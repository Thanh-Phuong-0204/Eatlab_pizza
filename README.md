# Hệ thống đếm doanh số bán pizza

Hệ thống này đếm số lượng pizza đã bán dựa trên video, sử dụng Ultralytics YOLO11 với class_id = 53 (Pizza)

## Tính năng
- Xác định vùng đếm
- Phát hiện và đếm pizza theo thời gian thực
- Thu thập phản hồi của người dùng để tinh chỉnh mô hình
- Được chứa hoàn toàn trong container bằng Docker Compose

## Run
Do video có dung lượng lớn nên cần thêm video vào path (video có tên 1465_CH02_20250607170555_172408.mp4 trong mục google drive đã lưu video từ path : https://drive.google.com/drive/folders/19QSILvBetBvcXyHjR85DahatiHOQSp_A)

sau đó

docker-compose up --build
