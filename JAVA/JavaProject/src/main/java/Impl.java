/**  
 * Project Name:JavaProject  
 * File Name:Impl.java  
 * Package Name:main.java  
 * Date:2018年1月2日下午10:09:51  
 * Copyleft (c) 2018, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main.java;  
/**  
 * ClassName:Impl <br/>  
 * Function: TODO ADD FUNCTION. <br/>  
 * Reason:   TODO ADD REASON. <br/>  
 * Date:     2018年1月2日 下午10:09:51 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */
interface I1 {  
    public default void print(){  
            System.out.println("I1");  
    }  
    public void hello();  
}  
interface I2{  
    public default void print(){  
            System.out.println("I2");  
    }  
    public void world();  
}  
public class Impl implements I1,I2{  
    public void hello(){  
    }  
    public void world(){  
    }
	@Override
	public void print() {
		  
		// 多继承？不可能的。必须覆盖掉。如果类Sub继承了两个接口，Base1和Base2，而这两个接口恰好具有完全相同的两个默认方法，那么就会产生冲突。这时Sub类就必须通过重载来显式指明自己要使用哪一个接口的实现（或者提供自己的实现）
		I1.super.print();
	}
	public static void main(String[] args) {
		Impl a =new Impl();
		a.print();
	}
}  
  
