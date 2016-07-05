package main.java;
/**
 * 数据类型基础知识
 */
public class Demo1 {

    public static void main(String[] args){
        // 定义类Demo1Student
    	class Demo1Student{  // 通过class关键字类定义类
    	    // 类包含的变量
    	    String name;
    	    int age;
    	    float score;

    	    // 类包含的函数
    	    void say(){
    	        System.out.println( name + "的年龄是 " + age + "，成绩是 " + score );
    	        }
    	}
    	class Demo2{//Java数据类型以及变量的定义
            // 字符型
            char webName1 = '赖';
            char webName2 = '尧';
            void name(){
            	System.out.println("作者的名字是：" + webName1 + webName2 );
            	}
            // 整型
            short x=22;  // 十进制短整型
            int y=022;  // 八进制整型
            long z=0x22L;  // 十六进制长整型
            // 浮点型
            float m = 22.25f;//单精度浮点型
            double n = 10.123123d;//双精度浮点型
            void number(){
            System.out.println("转化成十进制：x = " + x + ", y = " + y + ", z = " + z);
            System.out.println("计算乘积：" + m + " * " + n + "=" + m*n);
            // 强制数据类型转换
            System.out.println("丢失精度:a = (int)34.56 + (int)11.2=" + ((int)34.56 + (int)11.2) + " //丢失精度");
            System.out.println("提高精度:b = (double)m + (double)10 + 1=" + ((double)m + (double)10 + 1)+" //提高精度");
            }
    	}

        // 通过类来定义变量，即创建对象
    	Demo1Student stu1 = new Demo1Student();  // 必须使用new关键字
        // 操作类的成员
        stu1.name = "小明";
        stu1.age = 15;
        stu1.score = 92.5f;
        stu1.say();
        
        Demo2 demo=new Demo2();
        demo.name();
        demo.number();
    }
}