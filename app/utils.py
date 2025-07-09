import cv2

def draw_region(frame, region_points, color=(0, 255, 0)):
    cv2.polylines(frame, [region_points], isClosed=True, color=color, thickness=2)

def draw_count(frame, count):
    cv2.putText(frame, f"Pizza Count: {count}", (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
