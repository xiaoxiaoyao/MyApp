package main.java;

public class Demo2 {
//输出九九乘法表，经典FOR循环
	public static void main(String[] args) {
		int i,j;
		for(i=1;i<=9;i++){
			for(j=1;j<=i;j++){System.out.printf("%d*%d=%2d  ", i, j, i*j);}System.out.print("\n"); 
		}
	}
}
