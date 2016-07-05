package main.java;
/**
 * 
 * 继承是类与类之间的关系，是一个很简单很直观的概念，与现实世界中的继承（例如儿子继承父亲财产）类似。
 * 继承可以理解为一个类从另一个类获取方法和属性的过程。如果类B继承于类A，那么B就拥有A的方法和属性。
 * 继承使用 extends 关键字。
 * 
 */
public class ClassDemo {
    /**
     *  继承是在维护和可靠性方面的一个伟大进步。如果在 People 类中进行修改，那么 Teacher 类就会自动修改，而不需要程序员做任何工作，除了对它进行编译。
     */
    public static void main(String[] args) {
        Teacher t = new Teacher();
        t.name = "小尧";
        t.age = 25;
        t.school = "清华大学";
        t.subject = "Java";
        t.seniority = 999;
        t.say();
        t.lecturing();
        
    }
	/**
	 * 例如我们已经定义了一个类 People
	 */
    public static class People{
        String name;
        int age;
        int height;
        People(){
        	System.out.println("构造方法运行了一次");
        }
        void say(){
            System.out.println("我的名字是 " + name + "，年龄是 " + age + "，身高是 " + height);
        }
    }
    /**
     *  Teacher 是 People 的子类，People 是Teacher 类的父类。
     *  子类可以覆盖父类的方法。
     *  子类可以继承父类除private以为的所有的成员。
     *  构造方法不能被继承。
     */    
    public static class Teacher extends People{  // 先继承 People 类的成员，再增加自己的成员即可
         String school;  // 所在学校
         String subject;  // 学科
         int seniority;  // 教龄
         Teacher(){
        	 System.out.println("看，构造方法又运行了一次");
         }
         /**
          * 覆盖 People 类中的 say() 方法
          */
         void say(){
             System.out.println("我叫" + name + "，在" + school + "教" + subject + "，有" + seniority + "年教龄");
         }
        
         void lecturing(){
             System.out.println("我已经" + age + "岁了，依然站在讲台上讲课");
         }
     }    
}
