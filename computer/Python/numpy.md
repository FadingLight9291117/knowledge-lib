# axis的理解

关于numpy的axis，（pytorch的dim同理）

```python
arr = np.random(2,3) # 一个随机的2X3矩阵
arr.shape # (2,3)

a1 = arr.sum(axis=0)
a1.shape # (3,)

a2 = arr.sum(axis=1)
a2.shape # (2,)
```

这样可以明显看出来，`axis`去取什么值，在结果中那一维度的就“消失了”。