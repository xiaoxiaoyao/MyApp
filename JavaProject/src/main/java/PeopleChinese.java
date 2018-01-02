/**  
 * Project Name:JavaProject  
 * File Name:Chinese.java  
 * Package Name:main.java  
 * Date:2017年12月10日上午12:17:37  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main.java;  
/**  
 * ClassName:Chinese <br/>  
 * Function: implements是一个类，实现一个接口用的关键字，它是用来实现接口中定义的抽象方法。实现一个接口，必须实现接口中的所有方法。 <br/>  
 * (1)接口可以被多重实现（implements）,抽象类只能被单一继承（extends）
 * (2)接口只有定义,抽象类可以有定义和实现
 * (3)接口的字段定义默认为:public static final, 抽象类字段默认是"friendly"(本包可见)
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        PeopleInterface
 */
public class PeopleChinese implements PeopleInterface{
	
	
	@Override
	public void say() {
		/** 接口的实现:*/
		System.out.println(" 你好！");
	}
	public static void main(String[] arguments) {
		/**接口的调用：*/
		PeopleInterface chinese = new PeopleChinese() ;
		chinese.say();
		
		/** 接口的实现+调用,换成lambda表达式*/
		PeopleInterface english = () -> {System.out.println(" Hello!");};
		english.say();
}}
  
