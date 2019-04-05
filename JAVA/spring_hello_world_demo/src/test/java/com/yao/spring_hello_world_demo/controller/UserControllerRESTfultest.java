package com.yao.spring_hello_world_demo.controller;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.http.MediaType;
import org.springframework.mock.web.MockServletContext;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.RequestBuilder;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultHandlers;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration
public class UserControllerRESTfultest {

	private MockMvc mvc;

	@Before
	public void setUp() throws Exception {
		mvc = MockMvcBuilders.standaloneSetup(new UserControllerRESTfultest()).build();
	}

	@Test
	public void testUserControllerRESTful() throws Exception {
		// 测试UserControllerRESTful
		RequestBuilder request = null;

		// 1、get查一下user列表，应该为空
		mvc.perform(MockMvcRequestBuilders.get("/users/").accept(MediaType.APPLICATION_JSON))
				.andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print())
				.andExpect(content().string(equals("[]")));

		// 2、post提交一个user
		request = MockMvcRequestBuilders.post("/users/").param("id", "1").param("name", "测试大师").param("age", "20");
		mvc.perform(request).andExpect(content().string(equals("success")));

		// 3、get获取user列表，应该有刚才插入的数据
		request = MockMvcRequestBuilders.get("/users/");
		mvc.perform(request).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print())
				.andExpect(content().string(equals("[{\"id\":1,\"name\":\"测试大师\",\"age\":20}]")));

		// 4、put修改id为1的user
		request = MockMvcRequestBuilders.put("/users/1").param("name", "测试终极大师").param("age", "30");
		mvc.perform(request).andExpect(content().string(equals("success")));

		// 5、get一个id为1的user
		request = MockMvcRequestBuilders.get("/users/1");
		mvc.perform(request).andExpect(content().string(equals("{\"id\":1,\"name\":\"测试终极大师\",\"age\":30}")));

		// 6、del删除id为1的user
		request = MockMvcRequestBuilders.delete("/users/1");
		mvc.perform(request).andExpect(content().string(equals("success")));

		// 7、get查一下user列表，应该为空
		request = MockMvcRequestBuilders.get("/users/");
		mvc.perform(request).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print()).andExpect(content().string(equals("[]")));

	}

}