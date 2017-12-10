/**  
 * Project Name:JavaProject  
 * File Name:People.java  
 * Package Name:main.java  
 * Date:2017年12月10日上午12:20:01  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main.java;  
/**  
 * ClassName:People <br/>  
 * Function: 比如：People是一个接口，他里面有say这个方法。 <br/>  
 * 接口：初期理解,认为是一个特殊的抽象类。 <br/> 
 * 当抽象类中的方法都是抽象的，那么该类可以通过接口的形式来表示 <br/> 
 * class用于定义类 <br/> 
 * interface用于定义接口 <br/>  
 * 接口定义是,格式特点： <br/> 
 * 1.接口中常见定义:常量、抽象方法 <br/> 
 * 2.接口中成员都有固定修饰符 <br/> 
 *   常量： public static final <br/> 
 *   方法： public abstract <br/> 
 *    默认会补全，但为良好的阅读性，应写全） <br/> 
 *       接口中的成员都是public的 <br/> 
 * 接口是不可以创建对象的，因为有抽象方法。需要被子类实现。 <br/>  
 * Date:     2017年12月10日 上午12:20:01 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        PeopleChinese
 */
public interface PeopleInterface {
	/** 接口没有方法体。只能通过一个具体的类去实现其中的方法体 */
	public abstract void say();
	/**子类不可以覆盖父类的方法或者变量。即使子类定义与父类相同的变量或者函数，也会被父类取代掉。*/
	public static final int NUM = 3;
}
  
