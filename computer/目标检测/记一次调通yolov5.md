# 记一次调通yolov5

> 这次时隔四五个月吧，把yolov5捡起来再次调通跑了一次，发现最近官方代码更新的很频繁。
>
> 经过这几个月的学习，我发现自己已经能很轻易的看懂代码了。
>
> 下面就讲讲这次我从准备数据集到训练模型，测试模型的整个流程

## 1. 数据集

### 1.1 搜集数据

此处省略在如何网上搜集到的公开数据集...

简而言之，我在网上找到了一个公开的大型人脸数据集，叫[CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)，数据集包含202,599的人脸图像，一张图像包含一张人脸，以及对应的人脸标注，包括bound box和20余种属性(是否带眼睛，是否戴帽子等)。

我下载下来，然后写了个程序，取了200张图片带帽子的图片。

### 2. 标注数据

#### 2.1 标注工具

首先下载标注工具`labelme`，直接pip安装：

```shell
pip install labelme
```

在ubuntu上的话，也可以用apt安装：

```shell
sudo apt install labelme
```

完事直接标注图片，就是画框框住帽子

#### 2.2 标签转换

标注完后，要把标签转换成为yolo的标签格式。

labelme标注完后的标签格式是xml的，而yolov5的标签格式是这样的

```txt
0 0.12 0.32 0.3 0.41
```

每一张图片对应一个txt文件，图片中的每一个object对应一行5个值。

第一个值代表这个object的类别，后面四个值就是(x, y, w, h)，**注意这里是相对值**。

> 这里我想以后可以用微软的Vott来打标签，直接可以转YOLO的格式

#### 2.3 数据集配置文件

数据集准备完后，需要写一个数据集的yaml配置文件，下面这个是程序自带的coco数据集的配置文件

```yaml
# COCO 2017 dataset http://cocodataset.org - first 128 training images
# Train command: python train.py --data coco128.yaml
# Default dataset location is next to YOLOv5:
#   /parent
#     /datasets/coco128
#     /yolov5


# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: ../datasets/coco128  # dataset root dir
train: images/train2017  # train images (relative to 'path') 128 images
val: images/train2017  # val images (relative to 'path') 128 images
test:  # test images (optional)

# Classes
nc: 80  # number of classes
names: [ 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
         'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
         'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
         'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
         'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
         'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
         'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
         'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
         'hair drier', 'toothbrush' ]  # class names


# Download script/URL (optional)
download: https://github.com/ultralytics/yolov5/releases/download/v1.0/coco128.zip
```

就按照这个来组织我们的数据集路径，把数据集文件夹放在程序同一级目录的`datasets`目录下面，


