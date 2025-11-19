import json
import os

# 类别映射（类别名称到类别ID）
categories = {
    "cabbage": 0,
    "cutcabbag": 1
    # 添加其他类别
}

def convert_labelme_json_to_yolo(txt_path, json_path, img_width, img_height):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    annotations = data['shapes']
    yolo_labels = []

    for shape in annotations:
        label = shape['label']
        if label not in categories:
            continue  # 跳过未定义类别
        class_id = categories[label]

        points = shape['points']
        # 获取矩形左上角与右下角坐标
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)

        # 计算中心点和宽高（归一化）
        x_center = (xmin + xmax) / 2.0 / img_width
        y_center = (ymin + ymax) / 2.0 / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        yolo_labels.append(f"{class_id} {x_center} {y_center} {width} {height}")

    # 保存到txt文件
    with open(txt_path, 'w', encoding='utf-8') as f:
        for line in yolo_labels:
            f.write(line + '\n')

import os
json_files = [f for f in os.listdir('D:\\卷心菜cv识别\\视觉\\trans') if f.endswith('.json')]
for json_file in json_files:
# 使用示例
    image_width = 1024  # 替换为实际图片宽度
    image_height = 768  # 替换为实际图片高度
    convert_labelme_json_to_yolo("D:\\卷心菜cv识别\\视觉\\json-txt\\"+json_file.replace('.json','')+'.txt',
                                 "D:\\卷心菜cv识别\\视觉\\trans\\"+json_file, image_width, image_height)