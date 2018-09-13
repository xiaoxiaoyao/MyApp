package main.java;
/**
 * 参考http://www.mamicode.com/info-detail-517008.html
 *@functon 多线程学习 extends Thread
 *@author 小尧
 *@time 2016-10-17
 */
public class MutithreadLearningThread{
	public static void main(String args[]){
		MutiThreadsClass Thread1 = new MutiThreadsClass(),Thread2 = new MutiThreadsClass(),Thread3 = new MutiThreadsClass();
		Thread1.MutiThreads('a');
		Thread2.MutiThreads('b');
		Thread3.MutiThreads('c');
		/**
		 *易错：同一个Thread（extends Thread 线程类）不能重复调用start方法，会出现java.lang.IllegalThreadStateException异常。
		 *注意：start()方法的调用后并不是立即执行多线程代码，而是使得该线程变为可运行态（Runnable），什么时候运行是由操作系统决定的。
		 */
		Thread1.start();
		Thread2.start();
		Thread3.start();
	}
}
class MutiThreadsClass extends Thread{
		private char name;
		private int n=1;
		public int MutiThreads(char c){
			this.name=c;
			return 0;
		}
		public void run(){
			System.out.println(name + "(Thread)运行  :  " + n);
			n++;
			System.out.println(name + "运行  :  " + n);
			return;
		}
	

}

