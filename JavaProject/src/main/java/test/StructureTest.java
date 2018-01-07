/**  
 * Project Name:JavaProject  
 * File Name:StructureTest.java  
 * Package Name:main.java.test  
 * Date:2017年12月3日下午8:48:06  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main.java.test;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

import main.java.Structure;

class StructureTest {

	@Test
	void test() {
		String[] str = {"q","w"};
		Structure a = new Structure(str);
		a.show();
		Assert.assertEquals(a.next(), "q");
		Assert.assertEquals(a.next(), "w");
	}

}
  
