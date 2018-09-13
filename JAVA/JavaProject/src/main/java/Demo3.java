package main.java;
/** 
 * 
 * 方法内部除了能访问方法级的变量，还可以访问类级和实例级的变量。
 * 块内部能够访问类级、实例级变量，如果块被包含在方法内部，它还可以访问方法级的变量。
 * 方法级和块级的变量必须被显式初始化，否则不能访问。
 * @author yao
 */
public class Demo3 {
    public static String name = "yao";  // 类级变量（关键字static）
    public int i=1; // 对象实例级变量
    // 属性块，在类初始化属性时候运行
    {
		int j = 2;// 块级变量
        j=3;
        System.out.println("属性块，在类初始化属性时候运行"+"\n块级变量 j="+j);
    }
    
    public void test1() {
        int j = 3;  // 方法级变量
        if(j == 3) {
            int k = 5;  // 块级变量
            System.out.println("块级变量 k="+k);
        }
        // 这里不能访问块级变量，块级变量只能在块内部访问
        System.out.println("name=" + name + ",对象实例级变量 i=" + i + ", j=" + j);
    }
    
    public static void main(String[] args) {
        // 不创建对象，直接通过类名访问类级变量
        System.out.println(Demo3.name);
       
        // 创建对象并访问它的方法
        Demo3 t = new Demo3();
        t.test1();
    }
}
