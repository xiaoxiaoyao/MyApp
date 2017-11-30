package main.java;

public class NewRoot {
	static int num;
	public static void main(String[] args) throws java.lang.IllegalArgumentException,java.lang.ArithmeticException{
		if (args.length > 0) {
			try {
				num = Integer.parseInt(args[0]);
			}catch (NumberFormatException e){
				System.err.println("非数据类型不能转换。"); 
				throw new NumberFormatException("非数据类型不能转换。");
			}
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
