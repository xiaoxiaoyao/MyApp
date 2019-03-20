package com.yao.spring_hello_world_demo.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HomeController {

	@RequestMapping("/test")
	public String  Index(){
		return "hello world";
	}

}
