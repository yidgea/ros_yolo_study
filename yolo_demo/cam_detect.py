from ultralytics import YOLO
import cv2

# 加载预训练YOLOv8n模型
model = YOLO("yolov8n.pt")

# 打开USB摄像头，0代表第一个摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头！检查USB、权限")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 推理
    results = model(frame)
    # 绘制检测框
    annotated_frame = results[0].plot()
    
    # 显示画面
    cv2.imshow("YOLO USB Camera Detect", annotated_frame)
    
    # 按 q 退出窗口
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
