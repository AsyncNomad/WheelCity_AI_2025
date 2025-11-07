#!/usr/bin/env python3
import os, argparse
from pathlib import Path
from ultralytics import YOLO
from dotenv import load_dotenv

# --- 리포 루트 고정(이 파일: yolov8/train.py -> 루트는 parents[1])
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT  = SCRIPT_DIR.parent

# 루트의 .env를 확실히 로드
load_dotenv(REPO_ROOT / ".env")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model",    default=os.environ.get("YOLO_MODEL", "yolov8m.pt"))
    ap.add_argument("--data",     default=os.environ.get("YOLO_DATA", "yolov8/data.yaml"))
    ap.add_argument("--epochs",   type=int, default=int(os.environ.get("EPOCHS", "50")))
    ap.add_argument("--imgsz",    type=int, default=int(os.environ.get("IMGSZ", "640")))
    ap.add_argument("--batch",    type=int, default=int(os.environ.get("BATCH", "8")))
    ap.add_argument("--name",     default=os.environ.get("RUN_NAME", "ver1"))
    ap.add_argument("--patience", type=int, default=int(os.environ.get("PATIENCE", "10")))
    args = ap.parse_args()

    # 경로를 루트 기준 절대경로로 정규화
    model_path = (REPO_ROOT / args.model).resolve()
    data_path  = (REPO_ROOT / args.data).resolve()
    out_proj   = (REPO_ROOT / "yolov8" / "train_result").resolve()

    print("Starting training with the following configuration:")
    print(f"- Model: {model_path}")
    print(f"- Data: {data_path}")
    print(f"- Epochs: {args.epochs}")
    print(f"- Image Size: {args.imgsz}")
    print(f"- Batch Size: {args.batch}")
    print(f"- Patience: {args.patience}")
    print(f"- Run Name: {args.name}")

    model = YOLO(str(model_path))

    model.train(
        data=str(data_path),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        project=str(out_proj),
        name=args.name,
        patience=args.patience,
        pretrained=True,
    )
    print("Training finished.")
    print(f"Results saved to: {out_proj}/{args.name}")

if __name__ == "__main__":
    main()
