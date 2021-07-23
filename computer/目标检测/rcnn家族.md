# RCNN网络家族简介

```mermaid
graph LR;
    rcnn(RCNN)-->fast-rcnn(Fast-RCNN)-->faster-rcnn(Faster-RCNN)-->mask-rcnn(Mask-RCNN)
```

## RCNN

<img src="imgs/rcnn.png" alt="rcnn" style="zoom: 50%;" />

<img src="imgs/rcnn2.png" alt="rcnn2" style="zoom: 50%;" />

传统的滑动窗口算法，计算量巨大，RCNN为了解决这个问题，提出了`region proposal`(候选区域)这个概念。

具体的流程如下：
1. 对于一张图像，

## Fast-RCNN

<img src="imgs/fast-rcnn.png" alt="fast-rcnn" style="zoom: 50%;" />

## Faster-RCNN

<img src="imgs/faster-rcnn.png" alt="faster-rcnn" style="zoom:33%;" />




