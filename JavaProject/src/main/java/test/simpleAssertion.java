/**  
 * Project Name:JavaProject  
 * File Name:simpleAssertion.java  
 * Package Name:main.java.test  
 * Date:2017年12月1日上午12:12:43  
 *  
*/  
  
package main.java.test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;

/**  
 * ClassName:simpleAssertion <br/>  
 * Function: 简单测试，无需Function. <br/>  
 * Reason:   简单测试，无需REASON. <br/>  
 * Date:     2017年12月1日 上午12:12:43 <br/>  
 * @author   yao  
 * @version  0  
 * @since    JDK 1.6  
 */
class simpleAssertion {
	@Test
	@DisplayName("simple assertion")
	public void simple() {
	 assertEquals(3, 1 + 2, "simple math");
	 assertNotEquals(3, 1 + 1);
	 assertNotSame(new Object(), new Object());
	 Object obj = new Object();
	 assertSame(obj, obj);
	 assertFalse(1 > 2);
	 assertTrue(1 < 2);
	 assertNull(null);
	 assertNotNull(new Object());
}

}
  
