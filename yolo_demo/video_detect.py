from ultralytics import YOLO

model = YOLO("yolov8n.pt")
res = model("test.mp4", save=True, project="./results", name="video_out", exist_ok=True)
print("视频检测完成，结果在 ./results/video_out")
