/**  
 * Project Name:JavaProject  
 * File Name:Structure.java  
 * Package Name:main.java  
 * Date:2017年12月3日下午8:33:18  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main.java;

import java.util.ArrayList;

/**  
 * ClassName:Structure <br/>  
 * Function: 将相同类的对象存储到数组中. <br/>  
 * Date:     2017年12月3日 下午8:33:18 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */
public class Structure {
	static ArrayList<String> structure = new ArrayList<String>();
	static int n = -1;
	public Structure() {
		super();
	}
	public Structure(String[] args) {
		super();
		// TODO Auto-generated constructor stub  
		for(int i=0;i<args.length;i++) {
			structure.add(args[i]);
		}
	}
	public void show() {
		for(String name : structure) {
			System.out.println(name);
		}
	}
	public String next() {
		n++;
		return structure.get(n);
	}
	public static void main(String[] args) {
		
	}
}
  
