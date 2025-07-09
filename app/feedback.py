import os
import cv2

class FeedbackLogger:
    def __init__(self, save_dir="feedback_data"):
        os.makedirs(save_dir, exist_ok=True)
        self.save_dir = save_dir
        self.count = 0

    def save_frame(self, frame, reason="missed"):
        filename = f"{reason}_{self.count}.jpg"
        cv2.imwrite(os.path.join(self.save_dir, filename), frame)
        self.count += 1
