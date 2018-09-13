package main.java;

public class ThisDemo {
	/**
	 * 创建B类的对象b时，对B类的构造函数传入了A类的对象的引用（指针）
	 */
	public static void main(String[] args){
		new B(new A());
		//其实不需要写 B b =new B(new A());，直接这样写就可以体现。
		}

	static class A{
		/**
		 * 程序第一步会执行A类的构造方法A()，因为创建B类
		 * 的对象b时，对B类的构造函数传入了A类的对象的引用（指针），所以程序先执行
		 * new A() ，执行new A()的时候就运行了A类的构造方法。A类的构造方法里面
		 * 创建了B类的匿名对象，并且引用了B类匿名对象的print();方法。
		 */
		public A(){
			System.out.println("step 1 ");
			new B(this).print();
		}
		public void print(){
			System.out.println("step 3");//由于第二步a.print();执行了A类的
			//print()方法。所以程序第三步会运行到这里。
			System.out.println("hello from A");//然后执行到这句
			//代码，所以打印输出了hello from A
		}
	}
	static class B{
		A a;//这里先声明一个A类的对象a，这时还没有对a实例化，只是声明。
		public B(A a){//执行new A()完毕后，开始执行执行new B()了，这时会执行B类的
		//构造函数B()，
		this.a=a;//B b=new B(new A());//这里创建B类的对象b时，传入的A类对象
		//的引用（指针），赋予了之前声明的A类的对象a，这时a存储着创建B类的对象b时，传
		//入的A类对象的引用（指针）。
		}
		public void print()
		{ System.out.println("step 2 ");//由于引用了B类匿名对象的print()方法。
		//所以程序第二步会执行到这个方法里面。
		a.print();//因为a存储着创建B类的对象b时，传入的A类对象的引用（指针）。
		//所以这里执行a对象的方法print()，就是执行的A这个类里面的
		//print()方法。所以程序第二步会运行到这里。这里执行了A类的print()方法。
		//
		//打印输出hello from A完毕后，a.print();执行完毕，
		System.out.println("step 4 ");//所以开始执行这句
		System.out.println("hello from B");//和执行这句
		//整个程序结束在这里。
		}
	}
}