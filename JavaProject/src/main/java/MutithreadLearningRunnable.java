package main.java;
/**
 * 参考http://blog.csdn.net/evankaka/article/details/44153709#t1
 * 2018-01-02 update 使用匿名内部类改写一部分程序
 *@functon 多线程学习 extends Runnable
 *@author 小尧
 *@time 2016-10-18
 */
public class MutithreadLearningRunnable {
	public static void main(String args[]){
		// 这里用内部类修改啦一下
		Thread a =  new Thread(new Runnable(){
			private int n=0;
			public void run(){
				do{
					System.out.println("Thread a (Runnable)运行  :  " + n + " System.currentTimeMillis()=" + System.currentTimeMillis());
					try {
						Thread.sleep((int) Math.random() * 1000);
					} catch (InterruptedException e) {
						e.printStackTrace();
						break;
					} 
					n++;
				}while(n<3);
			}
		}
		);
		
		// 这里用匿名函数修改啦一下 注意这里用到啦箭头函数。在lambda表达式中，箭头操作符（->）右边语句为实现接口的方法
		Runnable runner = () -> { System.out.println("匿名函数 Thread b Runnable runner 运行啦" );};
		Thread b =new Thread(runner);
		
		a.start();
		b.start();
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
			System.out.println(name + "(Runnable)运行  :  " + n + " System.currentTimeMillis()=" + System.currentTimeMillis());
			try {
				Thread.sleep((int) Math.random() * 1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
				break;
			} 
			n++;
		}while(n<3);
	}
}