Developed a vision-based object tracking system using OpenCV to detect and track a moving object in real-time from a webcam feed. The pipeline includes grayscale conversion, thresholding, contour detection, and centroid estimation for robust object localization.

The detected object position is mapped from image space to Cartesian coordinates, which are then used to compute joint angles of a 3-DOF robotic arm using inverse kinematics. The system performs continuous frame-by-frame updates to enable real-time motion tracking and control.

Focused on the computer vision pipeline, including preprocessing (Gaussian blur), binary segmentation, contour extraction, and pixel-based centroid computation.