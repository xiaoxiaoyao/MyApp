package main.java;

public class Demo2 {

	public static void main(String[] args) {
		int i,j;
		for(i=1;i<=9;i++){
			for(j=1;j<=i;j++){System.out.printf("%d*%d=%2d  ", i, j, i*j);}System.out.print("\n"); 
		}
	}
}
