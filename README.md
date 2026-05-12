# Ball Tracker with Robotic Arm Control 🎯🤖

A real-time computer vision project that tracks a moving ball/object using a webcam and computes robotic arm joint angles using inverse kinematics. The detected object’s position is converted into servo motor angles and transmitted to an Arduino-controlled robotic arm for motion control.

This project combines **computer vision**, **inverse kinematics**, and **robotics control** into a live interactive system.

---

## Features ✨

* Real-time object/ball tracking using webcam
* Contour-based object detection
* Centroid calculation for object localization
* Inverse kinematics (IK) computation
* 3-DOF robotic arm angle generation
* Arduino servo motor control
* Live visualization of tracking and joint angles

---

## Tech Stack ⚙️

### Software

* Python
* OpenCV
* NumPy
* Math library
* Arduino IDE

### Hardware

* Webcam
* Arduino
* Servo Motors
* 3-DOF Robotic Arm

---

## How It Works 🧠

```text
Webcam Feed → Object Detection → Centroid Extraction → Inverse Kinematics → Servo Angles → Robotic Arm Motion
```

The system detects the largest object in the frame, computes its centroid and approximate depth, then calculates robotic arm joint angles using inverse kinematics.

---

## Core Concepts Used 📚

### Computer Vision

* Gaussian Blurring
* Thresholding
* Contour Detection
* Bounding Boxes
* Centroid Computation

### Robotics

* 3-DOF Inverse Kinematics
* Servo Angle Control
* Serial Communication with Arduino

---

## Installation 🚀

Clone the repository:

```bash
git clone https://github.com/ritisha2503/ball-tracker.git
cd ball-tracker
```

Install dependencies:

```bash
pip install opencv-python numpy
```

---

## Usage ▶️

### Python Side

Run the tracking script:

```bash
python main.py
```

### Arduino Side

1. Upload the `.ino` file to Arduino.
2. Connect servo motors to the specified PWM pins.
3. Start serial communication.

---

## Controls 🎮

| Key | Action           |
| --- | ---------------- |
| `q` | Quit application |

---

## Output Visualization 📸

The application displays:

* Thresholded object mask
* Contour visualization
* Bounding rectangle
* Object centroid
* Real-time servo angles

---

## Inverse Kinematics ⚡

The robotic arm angles are computed using trigonometric IK equations for a 3-link manipulator.

Joint angles generated:

* `theta1` → Base rotation
* `theta2` → Shoulder angle
* `theta3` → Elbow angle

---

## Project Structure 📂

```bash
ball-tracker/
│
├── main.py
├── winter_school.ino
├── README.md
└── requirements.txt
```

---

## Applications 💡

* Human-computer interaction
* Robotics automation
* Vision-guided robotic systems
* Industrial pick-and-place systems
* AI-assisted robotic control
* Motion tracking experiments

---

## Future Improvements 🌱

* Color-based object tracking
* PID-controlled smooth arm movement
* Multiple object tracking
* Depth camera integration
* YOLO/AI-based object detection
* Wireless robotic control

---

## Author 👩‍💻

Created by Ritisha Bajaj