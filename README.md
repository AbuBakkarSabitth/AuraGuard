# AuraGuard – Smart Workspace Monitor

AuraGuard is a real-time AI-powered workspace monitoring system that uses computer vision to improve productivity and well-being.

It detects phone distractions, tracks hydration habits, and monitors user presence using a webcam.

---

## Features

* Real-time object detection using YOLOv8
* Phone distraction detection
* Hydration monitoring (cup/bottle detection)
* User presence tracking
* Visual alerts and warnings
* FPS performance monitoring

---

## Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* COCO Dataset

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AuraGuard.git
cd AuraGuard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python auraguard.py
```

---

## How It Works

```
Webcam → YOLO Detection → Behavior Analysis → Alerts + HUD
```

---

## Future Improvements

* Posture detection
* Productivity analytics dashboard
* Mobile notifications
* Desktop application UI

---

## Author

MD Abu Bakkar Sabith
CSE Student, East Delta University
