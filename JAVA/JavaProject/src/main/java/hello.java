package main.java;
/**
 * http://blog.csdn.net/heavenying/archive/2007/05/31/1632348.aspx
 * lambda¸ÄÐ´³ÌÐò
 */
public class hello{
	public final static void main(String[] args) { 
		Runnable runner = () -> {System.out.println("Hello World! Hello lambda!");};
		runner.run();
	}
} 