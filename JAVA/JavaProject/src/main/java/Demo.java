package main.java;
/**
 * 父类行为被调用，就好象该行为是本类的行为一样，而且调用行为不必发生在父类中，它能自动向上层类追溯。
 * super 关键字的功能：
 *  调用父类中声明为 private 的变量。
 *  点取已经覆盖了的方法。
 *  作为方法名表示父类构造方法。
 * @author yaopr
 *
 */
public class Demo{
    public static void main(String[] args) {
    	//标记为static的方法不必new也可使用
    	Dog.alive();
    	//正常情况下需要new一个对象出来
        Dog obj = new Dog();
        obj.move();        
    }
}
class Animal{
    private String desc = "Animals are human's good friends";
    // 必须要声明一个 getter 方法
    public String getDesc() { return desc; }

    public void move(){
        System.out.println("Animals can move");
    }
    //标记为final的方法不可被覆盖
    public static final void alive() {
    	System.out.println("Animals alive");
    }
}
class Dog extends Animal{
	//标记为final的方法不可被覆盖
    public final void move(){
        super.move();  // 调用父类的方法
        System.out.println("Dogs can walk and run");
        // 通过 getter 方法调用父类隐藏变量
        System.out.println("Please remember: " + super.getDesc());
    }
    
}