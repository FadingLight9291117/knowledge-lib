# Go中的array和slice | Go主题月



## go的数组

**数组**是同一类型元素的固定长度的序列。

在go语言中一般不直接使用数组。



go语言中数组的声明：

```go
var a [3]int				// int数组默认为元素为0
var b = [...]int{1, 2, 3}	// 自动推断出数组的长度
var c = [...]int{2:3, 1:2}	// 使用引号，初始化指定位置的值
d := [...]int{1, 2, 4:5, 6}	
```



多维数组的声明：

```go
arr0 := [2][3]int{{1, 2, 3}, {4, 5, 10}}
arr1 := [...][3]int{{1, 2, 4}, {2, 3, 12}}	// 第二维不能省略
```



关于array的函数

```go
len(arr) == cap(arr)	// 都是求数组的长度
```



## go的切片

和数组对应的数据结构是slice，切片。

**切片**代表变长的序列。

slice的底层引用了一个array对象。



一个slice由三部分组成，指针，长度和容量。

![img](imgs\slice.png)

- 指针指向底层对应的数组，但一定是数组的第一个元素；
- 长度表示slice中元素的数目；
- 容量表示最大长度，所以长度不能超过容量。当向slice中添加元素超出cap后，就会重新分配底层数组。



### slice的创建

直接声明

```go
s1 := []int{2, 3, 4}	// len和cap都是3
s2 := []int{}			// 空slice
```



通过一个数组或者另一个slice

```go
arr := [...]int{2, 4, 5, 12, 5}

s1 := arr[0:2]
s2 := arr[:2]
s3 := arr[0:2:6] // [low:high:max]
```



通过make来创建slice

```go
var s2 []int = make([]int, 2, 5) 	// ptr, len, cap
s3 := make([]int, 2)				// 省略cap
```



### slice的相关操作

| 操作            | 含义                          |
| :-------------- | :---------------------------- |
| s[n]            | 返回索引n的元素               |
| s[:]            | 返回索引从0到len(s)-1的切片   |
| s[low:]         | 返回索引从low到len(s)-1的切片 |
| s[:high]        | 返回索引从0到high-1的切片     |
| s[low:high:max] | 返回索引从low到high-1的切片   |
| len(s)          | 返回切片的长度                |
| cap(s)          | 返回切片的容量                |



### 使用append函数追加元素

```go
s := []int{2, 3, 4}
append(s, 1, 2, 3)
```

当超过slice的容量的时候，会重新分配底层数组



### slice的拷贝, copy函数

复制长度以len最小的为准

```go
s1 := []int{2, 3, 4, 5}
s2 := make([]int, 2)
copy(s2, s1)
```





参考文献

1. http://www.topgoer.com
2. https://chai2010.cn/advanced-go-programming-book/ Go语言高级编程
3. https://docs.hacknode.org/gopl-zh/ Go语言圣经