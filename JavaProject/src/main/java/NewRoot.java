package main.java;

public final class NewRoot {
	static int num;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		if (args.length > 0) {
			num = Integer.parseInt(args[0]);
		}else {
			System.out.println("Please import a number");
			throw new java.lang.IllegalArgumentException("请输入一个数字");
		}
		if(num>=0) {
			System.out.println("The square root of " + num + " is " + Math.sqrt(num));
		}else {
			System.out.println("Please ?");
			throw new java.lang.ArithmeticException("请输入正数");
		}
	}
}
