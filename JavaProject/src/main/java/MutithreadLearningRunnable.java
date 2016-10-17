package main.java;
/**
 * 参考http://blog.csdn.net/evankaka/article/details/44153709#t1
 *@functon 多线程学习 extends Runnable
 *@author 小尧
 *@time 2016-10-18
 */
public class MutithreadLearningRunnable {
	public static void main(String args[]){
        new Thread(new MutiThreadsClassA('a')).start();  
        new Thread(new MutiThreadsClassA('b')).start(); 
	}
}
/**
 * Thread2类通过实现Runnable接口，使得该类有了多线程类的特征。run（）方法是多线程程序的一个约定。所有的多线程代码都在run方法里面。Thread类实际上也是实现了Runnable接口的类。
 * 在启动的多线程的时候，需要先通过Thread类的构造方法Thread(Runnable target) 构造出对象，然后调用Thread对象的start()方法来运行多线程代码。
 * 实际上所有的多线程代码都是通过运行Thread的start()方法来运行的。因此，不管是扩展Thread类还是实现Runnable接口来实现多线程，最终还是通过Thread的对象的API来控制线程的，熟悉Thread类的API是进行多线程编程的基础。
 *@author 小尧
 *@time 2016-10-18
 */
class MutiThreadsClassA implements Runnable{
	private int n=0;
	public char name;
	public MutiThreadsClassA(char c){
		this.name=c;
	}
	@Override
	public void run(){
		do{
			System.out.println(name + "(Runnable)运行  :  " + n);
			try {
				Thread.sleep((int) Math.random() * 1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} 
			n++;
		}while(n<10);
	}
}