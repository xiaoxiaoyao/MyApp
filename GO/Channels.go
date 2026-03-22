package main

import "fmt"

func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum // send sum to c
}

func fibonacci1(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
		fmt.Println("第", i, "个 For 循环中")
	}
	fmt.Println("close(c)")
	/* 	*注意：* 只有发送者才能关闭信道，而接收者不能。向一个已经关闭的信道发送数据会引发程序恐慌（panic）。
	*还要注意：* 信道与文件不同，通常情况下无需关闭它们。只有在必须告诉接收者不再有值需要发送的时候才有必要关闭，例如终止一个 range 循环。 */
	close(c)
}

func BufferedChannels() { //BufferedChannels()
	/*
	   带缓冲的信道
	   信道可以是 带缓冲的。将缓冲长度作为第二个参数提供给 make 来初始化一个带缓冲的信道：

	   ch := make(chan int, 100)
	   仅当信道的缓冲区填满后，向其发送数据时才会阻塞。当缓冲区为空时，接受方会阻塞。

	   修改示例填满缓冲区，然后看看会发生什么。(fibonacci会自动关闭信道)
	*/
	ch := make(chan int, 10)
	/* 	Go 程
	Go 程（goroutine）是由 Go 运行时管理的轻量级线程。 */
	go fibonacci1(cap(ch), ch)
	for i := range ch {
		fmt.Println(i)
	}
}

func Channels() { //Channels()
	fmt.Println("/*\n	   信道\n	   信道是带有类型的管道，你可以通过它用信道操作符 <- 来发送或者接收值。\n\n	   ch <- v    // 将 v 发送至信道 ch。\n	   v := <-ch  // 从 ch 接收值并赋予 v。\n	   （“箭头”就是数据流的方向。）\n\n	   和映射与切片一样，信道在使用前必须创建：\n\n	   ch := make(chan int)\n	   默认情况下，发送和接收操作在另一端准备好之前都会阻塞。这使得 Go 程可以在没有显式的锁或竞态变量的情况下进行同步。\n\n	   以下示例对切片中的数进行求和，将任务分配给两个 Go 程。一旦两个 Go 程完成了它们的计算，它就能算出最终的结果。\n	*/")
	s := []int{7, 2, 8, -9, 4, 0}

	c := make(chan int)
	/* 	Go 程
	Go 程（goroutine）是由 Go 运行时管理的轻量级线程。 */
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c // receive from c

	fmt.Println(x, y, x+y)
}
