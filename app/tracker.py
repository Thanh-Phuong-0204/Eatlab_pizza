import cv2
import numpy as np

class SimpleRegionTracker:
    def __init__(self, region_points):
        self.region = np.array(region_points, np.int32)
        self.count = 0
        self.previous_centers = []

    def track(self, detections):
        if not hasattr(detections, "boxes") or detections.boxes is None:
            return self.count

        current_centers = []

        for box in detections.boxes.xyxy:
            x_center = int((box[0] + box[2]) / 2)
            y_center = int((box[1] + box[3]) / 2)
            current_centers.append((x_center, y_center))

            if cv2.pointPolygonTest(self.region, (x_center, y_center), False) >= 0:
                # Check if it's a new object (not same as previous)
                if (x_center, y_center) not in self.previous_centers:
                    self.count += 1

        self.previous_centers = current_centers
        return self.count

