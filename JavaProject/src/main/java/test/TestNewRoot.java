package main.java.test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.TestInstance.Lifecycle;

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
}