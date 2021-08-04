
> 这里是我用go刷leetcode的一些感触

2021.07.27

1. 二叉树的遍历我居然还想了半天，还是要复习一下二叉树的先序中序后序遍历1)递归；2)非递归。以及深度优先，广度优先的递归和非递归。

2. 这点事关于go语言本身的

关于go中的slice，我在一个函数中发现了底层的错误用法。

看这个函数

```go
func preorder(root *TreeNode, res []*TreeNode) {
	if root == nil {
		return nil
	}
	res = append(res, root)
	preorder(root.Left, res)
	preorder(root.Right, res)
}
```

这个函数原本是树的先序遍历，原本的思路是：

函数第1个参数是一个二叉树，第2个参数是一个slice，我是想先序遍历二叉树，然后把每个node的指针依次存入`res`，
最后得到一个先序的slice。

但是问题是，最后得到的`res`是一个空的slice，也就是说这个函数不起作用，我首先想到的就是值传递问题，但是我发现问题不是这个。

问题出在这几行

```go
res = append(res, root)
preorder(root.Left, res)
preorder(root.Right, res)
```

这里第2行的递归函数并没有改变外面的`res`，究其原因，再看下面的代码

```go
a := make([]int, 1, 2)
a[0] = 1
b := append(a, 0)
fmt.Printf("%+v, len: %d, cap: %d.\n", a, len(a), cap(a))
fmt.Printf("%+v, len: %d, cap: %d.\n", b, len(b), cap(b))
```
output:
```
data: [1],   len: 1, cap: 2
data: [1 0], len: 2, cap: 2
```

这里原因就已经出来了，

slice内保存了一个数组的指针，而且在数组容量不够的时候会自动扩容，也就是整体复制到一个更大的内存空间；

**但是，slice本身并不是一个指针**，这就是问题所在，一个slice内不仅包含了数组指针，而且还存有`len`，`cap`这些属性，这俩属性可不是真实，就是int值，因此在传递函数的时候，这俩值并不会变，所以虽然底层的指针指向的数组长度变化了，但是在函数外的`res`长度并没有变化。

原因知道了，解决方案也比较简单，返回新的`res`就行了，用新的覆盖旧的，稍微改下就好了。

```go
func preorder(root *TreeNode, res []*TreeNode) []*TreeNode {
	if root == nil {
		return res
	}
	res = append(res, root)
	res = preorder(root.Left, res)
	res = preorder(root.Right, res)
	return res
}
```

完毕。

