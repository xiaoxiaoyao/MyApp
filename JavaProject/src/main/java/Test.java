package main.java;

public class Test {
	public static int i=1;
	//parent  
	public static class ParentStatic {  
	    public static void print(){  
	        System.out.println("************parent**************");  
	    }  
	  
	}  
	//child  
	public static class ChildStatic extends ParentStatic{  
	  
	    public static void print(){  
	        System.out.println("*******************child******************");
	        System.out.println(i);
	        ParentStatic.print();  
	        i=i+1;
//	                print(); //error occur,stack overflow  
//	        static方法是一个静态方法，在内存中的位置是在静态存储区。它可以用通过类名直接访问。而且不管声明了多少个类static方法只有一个，也就是说所有实例共用一个方法，而且static方法只能调用static方法。
	    }  
	}  
	public static class TestEntry {  
	    public static void main(String[] args) {//这个不运行的
	    	System.out.println("啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦");
	        ChildStatic.print();//you can also use "ChildStatic.print()" to access the "print()"  
	    }  
	    
	  
	}  

    public static void main(String[] args) {  
    	System.out.println("public static void main(String[] args) {  ");
        ChildStatic.print();//you can also use "ChildStatic.print()" to access the "print()"  
    }  
	  
}
