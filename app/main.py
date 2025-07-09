import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import cv2
import numpy as np
from app.detector import PizzaDetector
from app.tracker import SimpleRegionTracker
from app.counter import PizzaCounter
from app.feedback import FeedbackLogger
from app.utils import draw_region, draw_count

# REGION: Define region polygon by file region_points
region_points = np.array([
    (307, 342), (667, 327), (690, 486), (666, 660), (484, 656), (269, 658), (131, 609), (232, 452)
], np.int32)


# Init modules
detector = PizzaDetector()
tracker = SimpleRegionTracker(region_points)
counter = PizzaCounter()
feedback = FeedbackLogger()

cap = cv2.VideoCapture('D:\\Eatlab\\videos\\1465_CH02_20250607170555_172408.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter("D:\\Eatlab\\videos\\output.mp4", fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    detections = detector.detect(frame)
    count = tracker.track(detections)
    counter.update(count)

    # Draw overlay
    draw_region(frame, region_points)
    draw_count(frame, counter.get_total())

    # Show frame
    cv2.imshow("Pizza Counter", frame)
    video_writer.write(frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("f"):
        feedback.save_frame(frame, reason="user_feedback")

cap.release()
video_writer.release()
cv2.destroyAllWindows()
