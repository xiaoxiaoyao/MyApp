package main.java;
/**
 * <h1>重载：</h1>
 * <h3>说明：</h3>
 * <li>参数列表不同包括：个数不同、类型不同和顺序不同。</li>
 * <li>仅仅参数变量名称不同是不可以的。</li>
 * <li>跟成员方法一样，构造方法也可以重载。</li>
 * <li>声明为final的方法不能被重载。</li>
 * <li>声明为static的方法不能被重载，但是能够被再次声明。</li>
 * <h3>方法的重载的规则：</h3>
 * <li>方法名称必须相同。</li>
 * <li>参数列表必须不同（个数不同、或类型不同、参数排列顺序不同等）。</li>
 * <li>方法的返回类型可以相同也可以不相同。</li>
 * <li>仅仅返回类型不同不足以成为方法的重载。</li>
 * <h3>方法重载的实现：</h3>
 * <li>方法名称相同时，编译器会根据调用方法的参数个数、参数类型等去逐个匹配，以选择对应的方法，如果匹配失败，则编译器报错，这叫做重载分辨。</li>
 */
public class MethodOverloading {

    public static class Demo{
        /**
         * 一个普通的方法，不带参数
         */
        void test(){
            System.out.println("No parameters");
        }
        /**
         * 重载上面的方法，并且带了一个整型参数
         */
        void test(int a){
            System.out.println("a: " + a);
        }
        /**
         * 重载上面的方法，并且带了两个参数
         */
        void test(int a,int b){
            System.out.println("a and b: " + a + " " + b);
        }
        /**
         * 重载上面的方法，并且带了一个双精度参数
         */
        double test(double a){
            System.out.println("double a: " + a);
            return a*a;
        }
       
        public static void main(String args[]){
            Demo obj= new Demo();
            obj.test();
            obj.test(2);
            obj.test(2,3);
            obj.test(2.0);
        }
    }
}
