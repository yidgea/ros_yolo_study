from ultralytics import YOLO

# 加载刚才训练好的best权重
model = YOLO("runs/detect/train-3/weights/best.pt")

# 替换成你要测试的图片路径，比如val里的21.jpg
results = model.predict(source="my_dataset/images/val/21.jpg", save=True)
