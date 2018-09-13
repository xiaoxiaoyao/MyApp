/**  
 * Project Name:JavaProject  
 * File Name:FirstWebBean.java  
 * Package Name:main.java  
 * Date:2018年1月7日下午9:19:31  
 * Copyleft (c) 2018, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  

package main.java;

import java.util.Date;

import javax.jws.*;
import javax.jws.soap.SOAPBinding;
import javax.xml.ws.Endpoint;


/**  
 * ClassName:FirstWebBean <br/>  
 * Function: 简单的WEB服务 <br/>  
 * Reason:   学习WEB <br/>  
 * Date:     2018年1月7日 下午9:19:31 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */
public class FirstWebBean {
	public static void main(String[] arg) {
		FirstWebBeanImpl a = new FirstWebBeanImpl();
		Endpoint.publish("http://127.0.0.1:9999/a", a);
	}
}

@WebService()
class FirstWebBeanImpl implements SquareRootServer {
	@Override
	public double getSquareRoot(double inputNum) {
		return Math.sqrt(inputNum);
	}

	@Override
	final public String getTime() {
		final Date now = new Date();
		return now.toString();
	}
}
/**
 * The import javax.jws cannot be resolved in eclipse
 * <br/> I am using Eclipse Version: Oxygen.1a Release (4.7.1a). I am trying to create a web service application. but when i am trying to create an interface class with import javax.jws.WebService; i am getting error as "The import javax.jws cannot be resolved" <br/> <br/> when i replaced jdk 9 with jdk 8 in program files it worked.
 */

@WebService
@SOAPBinding()
interface SquareRootServer {	
	@WebMethod abstract double getSquareRoot(double inputNum);
	@WebMethod abstract String getTime();
}
