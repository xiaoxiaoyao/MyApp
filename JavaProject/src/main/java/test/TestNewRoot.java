package main.java.test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.*;
import main.java.NewRoot;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

class TestNewRoot {
	@Test
	@DisplayName("正常情况")
	void test() {
		ByteArrayOutputStream outContent = new ByteArrayOutputStream();  
        System.setOut(new PrintStream(outContent));  //这两行读取了控制台的输出，在断言部分只需要判断控制台的输出与我们的预期是否一致即可。
        String[] testInt = {"16"};
        NewRoot.main(testInt);
		assertEquals("The square root of 16 is 4.0\n",outContent.toString());
	}
	
	@Nested
	@DisplayName("异常输入")
	class hasException{
		@Nested
		@DisplayName("输入为空或输入字符")
		class errorTest{
	        @Test
	        @DisplayName("输入为空")
	        void isEmpty() {
	        	String[] testInt = {};
	        	
	            IllegalArgumentException exception = assertThrows(java.lang.IllegalArgumentException.class, () -> {
	            	NewRoot.main(testInt);
	            });
	            assertEquals("请输入一个数字", exception.getMessage());
	        }
	        @Test
	        @DisplayName("输入字符")
	        void isChar() {
	        	String[] testInt = {"A"};
	        	
	        	NumberFormatException exception = assertThrows(NumberFormatException.class, () -> {
	            	NewRoot.main(testInt);
	            });
	            assertEquals("非数据类型不能转换。", exception.getMessage());
	        }
		}
 
        @Test
        @DisplayName("输入负数")
        void throwsExceptionWhenPopped() {
        	String[] testInt = {"-1"};
        	ArithmeticException exception = assertThrows(java.lang.ArithmeticException.class, () -> {
        		NewRoot.main(testInt);
        		});
        assertEquals("请输入正数", exception.getMessage());
    }
    }
}