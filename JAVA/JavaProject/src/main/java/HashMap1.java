/**  
 * Project Name:JavaProject  
 * File Name:HashMap1.java  
 * Package Name:main.java  
 * Date:2017年12月15日上午12:31:30  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main.java;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

/**  
 * ClassName:HashMap1 <br/>  
 * Function: 开始学习HashMap <br/>  
 * Reason:   开始学习HashMap. <br/>  
 * Date:     2017年12月15日 上午12:31:30 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */
public class HashMap1 {
	private static HashMap<Serializable, Serializable> first = new HashMap<Serializable, Serializable>();
	private static HashMap<String,Long> phonebook =new HashMap<>();
	
	public static void main(String[] args) {
		// HashMap存储对象
		phonebook.put("MyPhoneNumber", 1234567890L);
		phonebook.put("PhoneNumber1", 11111L);
		phonebook.put("PhoneNumber2", 22222L);
		phonebook.put("MyPhoneNumber", 654321L);//如果key值一样会发生什么呢（看后面，被覆盖啦）
		first.put((String)"abc", (String)"def");
		first.put(123, 123);
		// HashMap读取对象
		Long a=phonebook.get("MyPhoneNumber");
		System.out.println("// HashMap读取对象 MyPhoneNumber " + a);
		a=phonebook.getOrDefault(null, -1L);
		System.out.println("// HashMap读取不存在的值null（使用 getOrDefault 避免返回null） " + a);
		// 统计size
		System.out.println(" phonebook.size(); " + phonebook.size());
		// 遍历对象（while，利用Iterator）
		final Iterator<Entry<String, Long>> iter = phonebook.entrySet().iterator();
		while (iter.hasNext()) {
			final Entry<String, Long> entry = iter.next();
			final Object key = entry.getKey();
			System.out.print(" key = entry.getKey(); " + key);
			final Object val = entry.getValue();
			System.out.println(" val = entry.getValue(); " + val);
		}
		// 遍历对象（按教科书）
		for (Map.Entry<String, Long> entry : phonebook.entrySet()){
			System.out.print(" entry.getKey(); " + entry.getKey());
			System.out.println(" entry.getValue(); " + entry.getValue());
		}
	}
}
  
