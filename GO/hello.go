package main

import (
	"fmt"
)

func sqrt(x float64) float64 {
	z := 0.0
	for i := 0; i < 1000; i++ {
		z -= (z*z - x) / (2 * x)
	}
	return z
}

func hello() {
	for i := 0; i < 3; i++ {
		defer fmt.Println(
			"hello, world. defer=",
			i)
	}
	defer fmt.Println("defer 语句会将函数推迟到外层函数返回之后执行。\n//推迟调用的函数其参数会立即求值，但直到外层函数返回前该函数都不会被调用。\n//推迟的函数调用会被压入一个栈中。当外层函数返回时，被推迟的函数会按照后进先出的顺序调用。")
	fmt.Printf("hello, world \n")
	fmt.Printf("Hello,world. Sqrt(2) = %v\n", sqrt(2))
}
