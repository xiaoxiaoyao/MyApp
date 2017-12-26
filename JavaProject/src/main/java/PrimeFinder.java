/**  
 * Project Name:JavaProject  
 * File Name:PrimeFinder.java  
 * Package Name:main.java  
 * Date:2017年12月17日下午8:27:08  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main.java;

import java.util.Scanner;

/**  
 * ClassName:PrimeFinder <br/>  
 * Function: 多线程练习 <br/>  
 * Reason:   学习多线程 <br/>  
 * Date:     2017年12月17日 下午8:27:08 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */
public class PrimeFinder implements Runnable {
	private static boolean isPrime(final int checkNumber) {
		double root = Math.sqrt(checkNumber);
		for (int i = 2 ; i <= root;i++) {
			if(checkNumber % i ==0) {
				return false;
			}
		}
		return true;
	}
	Thread go;
	private int numPrime;
	PrimeFinder(int numPrimes){
		super();
		this.setNumPrime(numPrimes);
        go = new Thread(this);
        //如果创建线程后立即运行，就直接go.run()
        //go.run();
	}
	public static Scanner sc = new Scanner(System.in); 
	public static void main(String[] args) {
        System.out.println("请输入一个数值（寻找1到输入数值范围内所有质数）："); 
        int maxNum ;
        maxNum = sc.nextInt(); 
        System.out.println("寻找1到"+ maxNum + "范围内所有质数"); 
        int numPrimes = 1;
		while(numPrimes<maxNum) {
	        PrimeFinder pf =new PrimeFinder(numPrimes);
	        //运行线程：go.start
	        pf.go.start();
			numPrimes++;
		}

	}

	@Override
	public void run() {
		int numPrime = this.getNumPrime();
		System.out.println("now num is " + numPrime);
		if(isPrime(numPrime)) {
			System.out.println(numPrime);
		}
	}

	/*Eclipse说了，要有Getter*/
	public int getNumPrime() {
		return numPrime;
	}

	/*Eclipse说了，要有Setter*/
	public void setNumPrime(int numPrime) {
		this.numPrime = numPrime;
	}

}
  
