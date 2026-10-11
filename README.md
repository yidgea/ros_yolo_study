
## 🛠️ 环境依赖
- Ubuntu 20.04 + ROS Noetic
- Python3
- ultralytics (YOLOv8)
- opencv-python

安装依赖：
```bash
pip install ultralytics opencv-python
```
图片检测
```
python3 yolo_demo/image_detect.py
```
摄像头实时监测
```
python yolo_demo/cam_detect.py
```
视频检测
```
python yolo_demo/video_detect.py
```
