import cv2

points = []

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Point added: ({x}, {y})")

# Load frame from video
cap = cv2.VideoCapture('D:\\Eatlab\\videos\\pizza.mp4')
ret, frame = cap.read()
cv2.imshow('Select Region Points', frame)
cv2.setMouseCallback('Select Region Points', draw_circle)

print("Click on the frame to select points. Press 'q' to quit.")
while True:
    temp_frame = frame.copy()
    for point in points:
        cv2.circle(temp_frame, point, 5, (0, 255, 0), -1)
    cv2.imshow('Select Region Points', temp_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print("Your region points:", points)
