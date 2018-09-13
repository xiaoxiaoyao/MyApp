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
 * Function: SalutonFrame之后学习监听事件 <br/>  
 * Reason:   学习 <br/>  
 * Date:     2017年12月6日 下午11:10:08 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;//使用ActionListener接口

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class SalutonFrameAction extends JFrame implements ActionListener {

	/**  
	 * serialVersionUID:系统说要加一个ID.  
	 * @since JDK 1.6  
	 */
	private static final long serialVersionUID = 1L;
	private static final int width=500, height=500; //写死窗口大小，开心就好
	static JButton okButton = new JButton("OK");//创建OK按钮
	static JLabel pageLabel = new JLabel("input something", JLabel.RIGHT);// 创建label
	static JTextField pageInput = new JTextField("default", 20);// 创建JTextField
	static JCheckBox jumbo1 = new JCheckBox("这是一个复选框", false);// 添加3个复选框
	static JCheckBox jumbo2 = new JCheckBox("这是一个复选框", false);
	static JCheckBox jumbo3 = new JCheckBox("这是一个选中的复选框", true);
	static ButtonGroup jumboGroup = new ButtonGroup();// 创建一个复选框的ButtonGroup
	
	public SalutonFrameAction() {
		super("Hellow World");//设置标题
		this.setSize(width, height);//设置窗口大小（后面就不写this啦）
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//设置为关闭窗口后退出
		FlowLayout flo = new FlowLayout();//设置窗口布局管理器FlowLayout
		setLayout(flo);//启用FlowLayout
		add(okButton);//添加OK按钮到界面
		add(pageLabel);//添加label到界面
		add(pageInput);//添加Text到界面
		jumboGroup.add(jumbo1);//把前面的这3个复选框放到一个group里面
		jumboGroup.add(jumbo2);
		jumboGroup.add(jumbo3);
		this.add(jumbo1);//添加3个复选框到界面
		this.add(jumbo2);//因为在构造函数里面，可以不加this
		this.add(jumbo3);
	}

	public static final void main(String[] args) {
		SalutonFrameAction frame = new SalutonFrameAction();
		frame.setVisible(true);//显示窗体
		okButton.addActionListener(frame);
	}

	@Override
	public void actionPerformed(ActionEvent event) {
		// TODO Auto-generated method stub  
		Object source = event.getSource();
		System.out.println(source);
	}

}
  
