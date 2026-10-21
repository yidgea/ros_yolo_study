from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data="dataset.yaml",
    epochs=10,
    imgsz=640,
    device="cpu",
    batch=1,
    workers=0
)

print("train done")
