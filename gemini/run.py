#!/usr/bin/env python3
import os, json, argparse, re
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT  = SCRIPT_DIR.parent

SYSTEM_PROMPT = (
    "You are an accessibility analysis AI. Analyze the provided image of a building entrance to determine if it is accessible for a lone wheelchair user.\n"
    "Accessibility Rules:\n"
    "1. There must be no steps or curbs between the ground and the entrance.\n"
    "2. If there are steps or curbs, a ramp must connect the ground to the entrance.\n\n"
    "Return ONLY valid JSON. Do not include any explanations, Markdown, or code fences.\n"
    'JSON schema: {"accessible": boolean | null, "reason": string}\n'
)

MIME_BY_EXT = {
    ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".png": "image/png", ".webp": "image/webp", ".bmp": "image/bmp",
}
SUPPORTED_EXTS = set(MIME_BY_EXT.keys())

def guess_mime(p: Path): return MIME_BY_EXT.get(p.suffix.lower())

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--images_dir", default="bbox_images")
    ap.add_argument("--out_json",   default="results/result.json")
    ap.add_argument("--model",      default=os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"))
    ap.add_argument("--timeout",    type=float, default=60.0)
    return ap.parse_args()

JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)
BRACE_SPAN_RE = re.compile(r"\{.*\}", re.DOTALL)

def try_extract_json(text: str) -> str | None:
    if not text: return None
    m = JSON_BLOCK_RE.search(text)
    if m: return m.group(1).strip()
    first, last = text.find("{"), text.rfind("}")
    if first != -1 and last != -1 and last > first:
        cand = text[first:last+1].strip()
        if cand.startswith("{") and cand.endswith("}"): return cand
    m2 = BRACE_SPAN_RE.search(text)
    return m2.group(0).strip() if m2 else None

def safe_json(text: str) -> dict:
    for candidate in (text, try_extract_json(text)):
        if not candidate: continue
        try:
            obj = json.loads(candidate)
            if not isinstance(obj, dict): raise ValueError()
            acc = obj.get("accessible", None)
            if acc not in (True, False, None): acc = None
            reason = obj.get("reason", "No reason provided.")
            if not isinstance(reason, str): reason = str(reason)
            return {"accessible": acc, "reason": reason}
        except Exception:
            pass
    return {"accessible": None, "reason": "Parse error: model did not return valid JSON."}

def main():
    # 루트의 .env를 확실히 로드
    load_dotenv(REPO_ROOT / ".env")

    args = parse_args()
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY (or GEMINI_API_KEY) is not set in repo-root .env")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=args.model,
        system_instruction=SYSTEM_PROMPT,
        generation_config={"response_mime_type": "application/json"},
    )

    images_dir = (REPO_ROOT / args.images_dir).resolve()
    out_json   = (REPO_ROOT / args.out_json).resolve()
    out_json.parent.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in images_dir.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS])
    if not files:
        raise RuntimeError(f"No images found under {images_dir} (supported: {sorted(SUPPORTED_EXTS)})")

    results = []
    for img_path in files:
        try:
            mime = guess_mime(img_path)
            if not mime:
                results.append({"image": img_path.name, "result": {"accessible": None, "reason": f"Unsupported extension: {img_path.suffix}"}})
                continue
            img_bytes = img_path.read_bytes()
            resp = model.generate_content([{"inline_data": {"mime_type": mime, "data": img_bytes}}],
                                          request_options={"timeout": args.timeout})
            text = getattr(resp, "text", "") or "".join(getattr(p, "text", "") for p in getattr(resp.candidates[0].content, "parts", []))
            results.append({"image": img_path.name, "result": safe_json((text or "").strip())})
        except Exception as e:
            results.append({"image": img_path.name, "result": {"accessible": None, "reason": f"Request error: {e}"}})

    out_json.write_text(json.dumps({"results": results}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Saved: {out_json}")

if __name__ == "__main__":
    main()
    