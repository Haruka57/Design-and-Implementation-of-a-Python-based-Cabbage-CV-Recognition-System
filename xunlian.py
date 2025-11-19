from ultralytics import YOLO

# 加载预训练模型
model = YOLO('yolov8n.pt')

# 训练参数配置 训练完成后会出现一个runs文件夹
results = model.train(
    data='D:\卷心菜cv识别\前端\dataset.yaml',
    epochs=1,
    imgsz=640,
    batch=16,
    name='safety_dyj'
)
