from ultralytics import YOLO
import cv2

class PizzaDetector:
    def __init__(self, model_path="models/yolo11n.pt", class_id=53, conf=0.25):
        self.model = YOLO(model_path)
        self.class_id = class_id
        self.conf = conf

    def detect(self, frame):
        results = self.model(frame, conf=self.conf, classes=[self.class_id])
        return results[0]
