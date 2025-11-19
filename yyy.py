import cv2
from ultralytics import YOLO

# 加载训练好的模型
model = YOLO('runs/detect/safety_dyj30/weights/best.pt')

# 测试单张图片
results = model.predict(
    source='da79a8fa41b5b235cedf2307163d3dc.jpg',
    conf=0.5,  # 置信度阈值
    save=True,  # 保存结果
    show_labels=True  # 显示标签
)

# 显示结果（可选）
for r in results:
    print(r)
    im_array = r.plot()  # 绘制检测框
    cv2.imshow('Detection', im_array)
    cv2.waitKey(0)
