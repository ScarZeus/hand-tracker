# Hand Track Counter

A real-time hand tracking  built with **MediaPipe Tasks API** and **OpenCV**. This project demonstrates a clean, production-ready setup for detecting and visualizing hand landmarks from a webcam feed, with a strong focus on correct architecture, performance, and maintainability.

---

## ✨ Features

* Real-time hand landmark detection
* Supports up to 2 hands simultaneously
* Clean OpenCV display (no UI flicker)
* Uses MediaPipe **HandLandmarker (.task model)**
* Stable VIDEO mode pipeline (easy to debug & extend)
* Modular project structure
* Ready for gesture recognition & finger counting

---

## 🧠 Tech Stack

* **Python** 3.10 – 3.12
* **MediaPipe** 0.10.14 (Tasks API)
* **OpenCV**
* **NumPy**

---

## 📁 Project Structure

```
hand-track-counter/
├── main.py                 # Application entry point
├── src/
│   └── track_hand.py       # Hand tracking logic
├── models/
│   └── hand_landmarker.task  # MediaPipe model (NOT committed)
├── venv/                   # Virtual environment (ignored)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/hand-tracker.git
cd hand-tracker
```

---

### 2️⃣ Create & activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install --upgrade pip
pip install mediapipe==0.10.14 opencv-python numpy
```

---

### 4️⃣ Download the MediaPipe model

The model is **not included** in the repository.

```bash
mkdir -p models
wget https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task -P models/
```

Expected path:

```
models/hand_landmarker.task
```

---

## ▶️ Running the Application

From the project root:

```bash
python3 main.py
```

Controls:

* Press **`q`** to quit the application

---

## 🖐 How It Works

1. OpenCV captures frames from the webcam
2. Frames are passed to MediaPipe HandLandmarker (VIDEO mode)
3. Hand landmarks are detected synchronously
4. Landmarks are drawn on the frame using MediaPipe drawing utilities
5. The annotated frame is displayed in real time

This architecture avoids async race conditions and ensures stable performance.

---

## 🚫 Ignored Files

The following are intentionally **not committed**:

* `venv/` (virtual environment)
* `models/*.task` (large binary model files)
* `__pycache__/`

See `.gitignore` for details.

---

## 🚀 Future Improvements

* Finger counting logic
* Gesture recognition
* FPS counter overlay
* Fullscreen / borderless display
* LIVE_STREAM mode for lower latency
* PyQt-based GUI
* Model configuration via YAML / ENV

---

## 🧪 Tested On

* Ubuntu 22.04+
* Python 3.12
* NVIDIA GTX 1650 (CPU inference supported)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

* [MediaPipe](https://developers.google.com/mediapipe)
* OpenCV community

---

## 📬 Contact

If you have suggestions or want to collaborate, feel free to open an issue or pull request.

Happy coding 🚀
