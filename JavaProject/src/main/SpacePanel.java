/**  
 * Project Name:JavaProject  
 * File Name:SpacePanel.java  
 * Package Name:main  
 * Date:2017年12月7日上午12:05:12  
 * Copyleft (c) 2017, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main;

import java.io.IOException;
import java.nio.file.*;
import javax.swing.*;

/**  
 * ClassName:SpacePanel <br/>  
 * Function: 显示总空间和剩余空间. <br/>  
 * Reason:   学习学习. <br/>  
 * Date:     2017年12月7日 上午12:05:12 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        
 */
public class SpacePanel extends JPanel{
	/**  
	 * serialVersionUID:系统说要加一个ID.  
	 * @since JDK 1.6  
	 */
	private static final long serialVersionUID = 1L;
	JLabel spaceLabel = new JLabel("Disk space:");
	JLabel space = new JLabel();
	public SpacePanel() {
		super();
		try {
			setValue();
		}catch(IOException ioe) {
			space.setText("Error");
		}
	}
	private void setValue() throws IOException {
		//获取当前磁盘
		Path current = Paths.get("");
		FileStore store =Files.getFileStore(current);
		//获取当前磁盘空间情况
		long totalSpace = store.getTotalSpace();
		long freeSpace = store.getUsableSpace();
		space.setText("totalSpace is " + totalSpace + " freeSpace is " + freeSpace);
	}

}
  
