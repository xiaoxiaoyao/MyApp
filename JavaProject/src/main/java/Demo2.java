package main.java;
import java.util.*;

public class Demo2 {
private static Scanner sc;
	//输出九九乘法表，经典FOR循环
	public static void main2(String[] args) {
		int i,j;
		for(i=1;i<=9;i++){
			for(j=1;j<=i;j++){System.out.printf("%d*%d=%2d  ", i, j, i*j);}System.out.print("\n"); 
		}
	}
    public static void main(String[] args){
        int intArray[] = new int[5];
        long total = 0;
        int len = intArray.length;
       
        // 给数组元素赋值
        System.out.print("请输入" + len + "个整数，以空格为分隔：");
        sc = new Scanner(System.in);
        for(int i=0; i<len; i++){
            intArray[i] = sc.nextInt();
        }
       
        // 计算数组元素的和
        for(int i=0; i<len; i++){
            total += intArray[i];
        }
       
        System.out.println("所有数组元素的和为：" + total);
    }
}
