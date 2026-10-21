
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not cap.isOpened():
    raise RuntimeError("无法打开摄像头，请检查 /dev/video0")

# 按摄像头支持的模式设置
cap.set(cv2.CAP_PROP_FOURCC,
        cv2.VideoWriter_fourcc(*"MJPG"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 15)

fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
fmt = "".join(chr((fourcc >> (8 * i)) & 255)
              for i in range(4))

print("实际格式:", fmt)
print("实际分辨率:",
      cap.get(cv2.CAP_PROP_FRAME_WIDTH),
      "x",
      cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("读取失败")
        break

    cv2.imshow("Raw Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

