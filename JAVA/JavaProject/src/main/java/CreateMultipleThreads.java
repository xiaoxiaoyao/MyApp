package main.java;

/**
 * Create multiple threads.
 * @author yaopr
 *
 */
class NewThreadTest implements Runnable {
    /**
     * name of thread
     */
	String name; 
	private int i=0;
	Thread t;
    NewThreadTest(String TreadName){
    	name=TreadName;
    	t = new Thread(this,name);
    	t.start();
    }
	public void run() {
		try{
			System.out.println("This thread name is :" + name);
			for(i=1;i<5;i++){
				Thread.sleep(100);
				System.out.println("This thread name is :" + name + " and i is " + i);				
			}
		}catch(Throwable e){
			 System.out.println(name + "Throwable" + e);
		}finally{
	         System.out.println(name + " exiting.");
		}
	}
}
/**
 * 通常你希望主线程最后结束。在前面的例子中，这点是通过在main()中调用sleep()来实现的，经过足够长时间的延迟以确保所有子线程都先于主线程结束。然而，这不是一个令人满意的解决方法，它也带来一个大问题：一个线程如何知道另一线程已经结束？
 * 幸运的是，Thread类提供了回答此问题的方法。
 * 两种方法可以判定一个线程是否结束。第一，可以在线程中调用isAlive()。这种方法由Thread定义，它的通常形式如下：
 *   final boolean isAlive( )
 * 如果所调用线程仍在运行，isAlive()方法返回true，如果不是则返回false。
 * 等待线程结束的更常用的方法是调用join()，描述如下：
 *   final void join( ) throws InterruptedException
 * 该方法等待所调用线程结束。该名字来自于要求线程等待直到指定线程参与的概念。join()的附加形式允许给等待指定线程结束定义一个最大时间。
 * @author yaopr
 *
 */
public class CreateMultipleThreads {
	public static void main(String args[]) {
		try{
			for(int i=0;i<6;i++){
				System.out.println("New Thread: " + i);
				NewThreadTest ts=new NewThreadTest("Thread" + i );//创建线程
				ts.t.join(50);
				System.out.println("Thread " + ts.name + " is alive?" + ts.t.isAlive() + "Creat and Join" + i);//isAlive（）很少用到，等待线程结束的更常用的方法是调用join()
				ts.t.join(50);//join()方法等待所调用线程结束。该名字来自于要求线程等待直到指定线程参与的概念。join()的附加形式允许给等待指定线程结束定义一个最大时间。比如50ms
				}
		}catch(InterruptedException e){
			System.out.println(e);
		}finally{
        System.out.println("main exiting.");
        }
	}
}