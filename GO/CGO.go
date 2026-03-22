package main

/*一个最简的CGO程序-基于C标准库函数输出字符串*/

//#include <stdio.h>
import "C"

func CGO() {
	C.puts(C.CString("Hello, World\n"))
}
