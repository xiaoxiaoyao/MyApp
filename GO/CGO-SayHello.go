package main

/*
#include <stdio.h>
static void SayHello(const char* s){
	printf("SayHello\n");
	puts(s);
}
*/
import "C"

func SayHello() {
	C.SayHello(C.CString("hello"))
}
