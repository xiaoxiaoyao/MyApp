package main.java;

class Q {
 int n;
 boolean valueSet = false;
 synchronized int get() {
     if(!valueSet)
         try {
             wait();
         } catch(InterruptedException e) {
             System.out.println("InterruptedException caught");
         }
         System.out.println("Got: " + n);
         valueSet = false;
         notify();
         return n;
     }
     synchronized void put(int n) {
         if(valueSet)
         try {
             wait();
         } catch(InterruptedException e) {
             System.out.println("InterruptedException caught");
         }
         this.n = n;
         valueSet = true;
         System.out.println("Put: " + n);
         notify();
     }
 }
 class Producer implements Runnable {
     Q q;
     Producer(Q q) {
     this.q = q;
     new Thread(this, "Producer").start();
 }
 public void run() {
     int i = 0;
     while(true) {
         q.put(i++);
     }
 }
}
class Consumer implements Runnable {
 Q q;
 Consumer(Q q) {
     this.q = q;
     new Thread(this, "Consumer").start();
 }
 public void run() {
     while(true) {
         q.get();
     }
 }
}
/*
 *  用Java正确的编写该程序是用wait( )和notify( )来对两个方向进行标志，如下所示：
 *  A correct implementation of a producer and consumer.
 */
class PCFixed {
 public static void main(String args[]) {
	 Q q = new Q();
     new Producer(q);
     new Consumer(q);
     System.out.println("Press Control-C to stop.");
	 
 }
}