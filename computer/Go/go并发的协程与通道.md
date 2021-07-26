# Go并发的协程与通道

> 不要通过共享内存来通信，而通过通信来共享内存。

## Go协程goroutine

什么是`goroutine`?

`goroutine`是go语言中的`协程`。

那什么是`协程`?

有人把`协程(routine)`称为轻量级的`线程`，所谓轻量即耗费更少的资源。

又来一个问题，什么是`线程`？

`线程(thread)`是CPU调度的最小单位，是允许应用程序并发执行多个任务的一种机制。

那这里又有一个概念，`进程`，进程是什么？

`进程(process)`是CPU分配资源的最小单位，一个正在运行的程序就是一个进程。

所以现在梳理一下关系：

一个进程中可以包含多个线程，一个线程中可以包含多个协程，而不管是进程、线程、协程都是程序并发执行的一种方式。

但是协程与进程和线程的最大区别就是协程的切换是由程序控制的，而进程和线程的切换则是由操作系统控制的，因此多进程和多协程在切换时需要由CPU来调度，它们的切换都会消耗较多的资源。由于协程的调度完全是由用户通过程序来控制，所以协程更加灵活更加轻量。而用协程来实现并发将会是一种更好的方式。

## goroutine的使用

goroutine的使用非常简单，只需要在普通函数调用时，在其前面加上`go`关键字即可将普通函数变为一个协程。

```go
func main() {
	for i := 0; i < 10; i++ {
		go AFun(i)
	}
	time.Sleep(10 * time.Second)
}

func AFun(i int) {
	fmt.Printf("fun%d begin...\n", i)
	time.Sleep(1 * time.Second)
	fmt.Printf("fun%d end.\n", i)
}
```

这样就实现了创建10个协程并行运算。

## 使用通道channel来实现协程通信

协程协程，相互协作的程序，那协作难免要相互传递数据。而在go中，提供了channel来进行goroutine间传递数据。

channel就类似一个队列，可以将数据输入到channel中，然后可以从通道中取出数据。

```go
var g = make(chan int)

func routine1() {
	g <- 10
	fmt.Println("goroutine 1 done.")
}

func routine2() {
	var1 := <-g
	fmt.Println(var1)
	fmt.Println("goroutine 2 done.")
}

func main() {
	defer close(g)

	go routine2()
	go routine1()
```

在这段代码中第一行创建了一个channel，channel的类型是`chan`，而chan中存储的数据为int类型

在函数`routine1`中的第一行

```go
	g <- 10
```

将10传入通道

而函数`routine2`中

```go
var1 := <-g 
```

则是从chan中取出数据，存入变量

这样一存一取，就构成了一个简单的生产者-消费者模型，也就实现了协程间传递数据。

### channel的类型

```go
ch2 := make(chan int, 10)
```

通过make可以给chan分配缓存，即chan中最多存储的数据量。这样的chan被成为带缓存的chan。

而

```go
ch1 := make(chan int, 0)
ch1 := make(chan int)
```

则被成为无缓存的chan

还有一个类型叫做`单向通道`

```go
//单向通道
func foo1(out chan<- int) {
	out <- 10
}

func foo2(in <-chan int) {
	var1 := <-in
	fmt.Println(var1)
}
```

`chan<-`只能存

`<-chan`只能取