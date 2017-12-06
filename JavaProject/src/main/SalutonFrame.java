/**  
 * Project Name:JavaProject  
 * File Name:SalutonFrame.java  
 * Package Name:main  
 * Date:2017年12月6日下午11:10:08  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  

package main;  
/**  
 * ClassName:SalutonFrame <br/>  
 * Function: 学习使用窗体、组件，制作用户界面 <br/>  
 * Reason:   学习 <br/>  
 * Date:     2017年12月6日 下午11:10:08 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */

import java.awt.FlowLayout;
import javax.swing.*;

public class SalutonFrame extends JFrame {

	/**  
	 * serialVersionUID:系统说要加一个ID.  
	 * @since JDK 1.6  
	 */
	private static final long serialVersionUID = 1L;

	public SalutonFrame() {
		super("Hellow World");//设置标题
		setSize(500,500);//设置窗口大小
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//设置为关闭窗口后退出
		FlowLayout flo = new FlowLayout();//设置窗口布局管理器FlowLayout
		setLayout(flo);//启用FlowLayout
		JButton okButton = new JButton("OK");//创建OK按钮
		add(okButton);//添加OK按钮到界面
		JLabel pageLabel = new JLabel("input something",JLabel.RIGHT);//创建label
		add(pageLabel);//添加label到界面
		JTextField pageInput = new JTextField("default",20);
		add(pageInput);//添加Text到界面
		JCheckBox jumbo1 = new JCheckBox("这是一个复选框",false);//添加3个复选框
		JCheckBox jumbo2 = new JCheckBox("这是一个复选框",false);
		JCheckBox jumbo3 = new JCheckBox("这是一个选中的复选框",true);
		ButtonGroup jumboGroup = new ButtonGroup();//把这3个复选框放到一个group里面
		jumboGroup.add(jumbo1);
		jumboGroup.add(jumbo2);
		jumboGroup.add(jumbo3);
		this.add(jumbo1);//添加3个复选框到界面
		this.add(jumbo2);//因为在构造函数里面，可以不加this
		this.add(jumbo3);
	}

	public static void main(String[] args) {
		SalutonFrame frame = new SalutonFrame();
		SpacePanel spaceLanel = new SpacePanel();//显示磁盘空间
		frame.add(spaceLanel.spaceLabel);
		frame.add(spaceLanel.space);
		frame.setVisible(true);//显示窗体
	}

}
  
