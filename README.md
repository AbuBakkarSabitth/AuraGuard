# 🚀 AuraGuard - Smart Workspace & Hydration Monitor

AuraGuard is a real-time AI-powered desktop productivity assistant that monitors workspace behavior using computer vision.

It helps users stay focused, avoid distractions, and maintain healthy habits while working.

---

## ✨ Features

- 📱 Phone distraction detection (real-time alerts)
- 💧 Hydration monitoring (cup/bottle detection)
- 👤 User presence detection (away vs focusing)
- ⚡ Real-time performance with FPS tracking
- 🔒 Privacy-first (runs fully locally)

---

## 🧠 How It Works

AuraGuard uses a webcam feed and processes it using a YOLO (You Only Look Once) object detection model.

Workflow:

Webcam → YOLO Detection → Behavior Analysis → Smart Alerts → UI Display

---

## 🛠 Tech Stack

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- COCO Dataset

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/AbuBakkarSabith/AuraGuard.git
cd AuraGuard
