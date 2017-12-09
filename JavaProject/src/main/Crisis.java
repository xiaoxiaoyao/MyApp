/**  
 * Project Name:JavaProject  
 * File Name:Crisis.java  
 * Package Name:main  
 * Date:2017年12月9日下午7:54:46  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  

package main;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

/**  
 * ClassName:Crisis <br/>  
 * Function: 学习用户界面布局<br/>  
 * Reason:   ADD REASON. <br/>  
 * Date:     2017年12月9日 下午7:54:46 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */

public class Crisis extends JFrame {
	/**  
	 * serialVersionUID:版本控制，确保版本一样用.  
	 * @since JDK 1.6  
	 */
	private static final long serialVersionUID = 1L;
	private static final int width=500, height=500; //写死窗口大小，开心就好
	private static final String lookAndFeel = "com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel";
	public Crisis() {
		super();
		JPanel row = new JPanel();
		this.setSize(width, height);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//设置点击关闭退出
		FlowLayout flo = new FlowLayout();
		row.setLayout(flo);
		ArrayList<JButton> buttons = new ArrayList<JButton>(5);//用数组管理按钮
		buttons.add(new JButton("Panic"));//批量添加按钮
		buttons.add(new JButton("Don't Panic"));
		buttons.add(new JButton("Blame Others"));
		buttons.add(new JButton("Notify the Media"));
		buttons.add(new JButton("Save Yourself"));
		for (JButton button:buttons) {
			row.add(button);//批量添加到用户界面
		}
		this.add(row);
		this.setVisible(true);
	}
	public Insets getInsets() {
		Insets squeeze = new Insets(100,50,20,0);//上左下右边框距离，覆盖 getInsets()方法
		return squeeze;
	}
	private static void setLookAndFeel() {
		  try {
			  UIManager.setLookAndFeel(lookAndFeel);
		  }catch(Exception exc) {
			  System.out.println(exc);//输出错误，继续运行程序
		  }
	}
	public static final void main(String[] arguments) {
		Crisis.setLookAndFeel();
		@SuppressWarnings("unused")
		Crisis frame =new Crisis();
	}

}
  
