/**  
 * Project Name:JavaProject  
 * File Name:KeyView.java  
 * Package Name:main  
 * Date:2017年12月11日上午12:52:48  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main;

import java.awt.BorderLayout;
import java.awt.GraphicsConfiguration;
import java.awt.HeadlessException;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

/**  
 * ClassName:KeyView <br/>  
 * Function: TODO ADD FUNCTION. <br/>  
 * Reason:   TODO ADD REASON. <br/>  
 * Date:     2017年12月11日 上午12:52:48 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */
public class KeyView extends JFrame implements KeyListener {

	/**  
	 * serialVersionUID:总有这个东西的.  
	 * @since JDK 1.6  
	 */
	private static final long serialVersionUID = 1L;
	public JTextField keyText = new JTextField(80);
	public JLabel keyLabel = new JLabel("Press any key in the text field");
	public BorderLayout bord = new BorderLayout();
	private static final int width=500, height=500; //写死窗口大小，开心就好
	private void KeyViewer() {
		SalutonFrame.setLookAndFeel();
		this.setSize(width, height);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		keyText.addKeyListener(this);
		this.setLayout(bord);
		this.add(keyLabel,BorderLayout.NORTH);
		this.add(keyText,BorderLayout.CENTER);
	}
	public KeyView() throws HeadlessException {
		super("KeyView");
		KeyViewer();
	}
	public KeyView(GraphicsConfiguration arg0) {
		super(arg0);
		KeyViewer();
	}

	public KeyView(String arg0) throws HeadlessException {
		super(arg0);
		KeyViewer();
	}

	public KeyView(String arg0, GraphicsConfiguration arg1) {
		super(arg0, arg1);
		KeyViewer();
	}

	public static void main(String[] args) {
		KeyView frame =new KeyView();
		frame.setVisible(true);
	}

	@Override
	public void keyPressed(KeyEvent txt) {
		System.out.println("keyPressed" + txt);
	}

	@Override
	public void keyReleased(KeyEvent txt) {
		System.out.println("keyReleased" + txt);
	}

	@Override
	public void keyTyped(KeyEvent txt) {
		System.out.println("keyReleased" + txt);
	}

}
  
