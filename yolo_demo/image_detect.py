from ultralytics import YOLO

# 加载yolov8n模型，使用本地yolov8n.pt
model = YOLO("yolov8n.pt")

# 对bus.jpg图片做检测，结果保存到results/img_out
res = model("bus.jpg", save=True, project="./results", name="img_out", exist_ok=True)

print("✅图片检测完成！结果图片保存在 results/img_out 文件夹内")
