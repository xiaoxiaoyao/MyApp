package main.java;

public class CurrentThreadDemo {
	/** Controlling the main Thread.
	 * 
	 */
    public static void ThreadDemo(){
        Thread t = Thread.currentThread();
        System.out.println("Current thread: " + t);
        // change the name of the thread
        t.setName("My Thread");
        System.out.println("After name change: " + t);
        try {
            for(int n = 5; n > 0; n--) {
                System.out.println(n);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("Main thread interrupted");
        }
    }
    public static void main(String args[]) {
    	new NewThread();
    	ThreadDemo();
    }
}
/**
 * 下面的例子是创建一个新的线程并启动它运行：
 * // Create a second thread.
 */
class ThreadDemo {
	    private NewThread thread;

		public void main(String args[]) {
	        thread = new NewThread();
	        thread.t.setPriority(Thread.MIN_PRIORITY);//设置优先级
	        try {
	            for(int i = 5; i > 0; i--) {
	                System.out.println("Main Thread: " + i);
	                Thread.sleep(1000);
	            }
	        } catch (InterruptedException e) {
	           System.out.println("Main thread interrupted.");
	        }
	        System.out.println("Main thread exiting.");
	    }
}

class NewThread implements Runnable {
    Thread t;
    NewThread() {
        /** Create a new, second thread */
        t = new Thread(this, "Demo Thread");
        System.out.println("Child thread: " + t);
        t.start(); // Start the thread
    }

    // This is the entry point for the second thread.
    public void run() {
        try {
            for(int i = 5; i > 0; i--) {
                System.out.println("Child Thread: " + i);
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
            System.out.println("Child interrupted.");
        }
        System.out.println("Exiting child thread.");
    }
}
