#!/usr/bin/env python3
import argparse
from pathlib import Path
from ultralytics import YOLO

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT  = SCRIPT_DIR.parent

def main():
    ap = argparse.ArgumentParser()
    # 기본값은 repo 루트 기준으로 해석되도록 문자열만 두고, 밑에서 절대경로화
    ap.add_argument("--weights", default="yolov8/train_result/ver14/weights/best.pt")
    ap.add_argument("--source",  default="input_images")
    ap.add_argument("--outdir",  default="bbox_images")
    ap.add_argument("--imgsz",   type=int, default=640)
    ap.add_argument("--conf",    type=float, default=0.25)
    args = ap.parse_args()

    weights = (REPO_ROOT / args.weights).resolve()
    source  = (REPO_ROOT / args.source).resolve()
    outdir  = (REPO_ROOT / args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    model = YOLO(str(weights))
    model.predict(
        source=str(source),
        imgsz=args.imgsz,
        conf=args.conf,
        save=True,
        project=str(outdir),
        name=".",           # outdir 바로 아래에 저장
        exist_ok=True,
        line_width=2,
        device="cpu"        # 필요 시 "cpu"/0 선택 가능. 자동 선택 원하면 이 줄 제거.
    )
    print(f"[OK] Saved bbox images to: {outdir}")

if __name__ == "__main__":
    main()
    