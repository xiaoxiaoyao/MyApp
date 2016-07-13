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
	private String name; 
	private int i=0;
	private Thread t;
    NewThreadTest(String TreadName){
    	name=TreadName;
    	t = new Thread(this,name);
    	t.start();
    }
	public void run() {
		try{
			System.out.println("Thread name is :" + name);
			for(i=1;i<5;i++){
				Thread.sleep(100);
				System.out.println("Thread name is :" + name + " and i is " + i);				
			}
		}catch(Throwable e){
			 System.out.println(name + "Throwable" + e);
		}finally{
	         System.out.println(name + " exiting.");
		}
	}
}
public class CreateMultipleThreads {
	public static void main(String args[]) {
		try{
		for(int i=1;i<10;i++){
			System.out.println("main: " + i);
			new NewThreadTest("Thread" + i );//创建线程
			}
		}finally{
        System.out.println("main exiting.");
        }
	}
}