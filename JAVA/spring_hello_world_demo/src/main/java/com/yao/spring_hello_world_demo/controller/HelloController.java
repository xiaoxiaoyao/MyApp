package com.yao.spring_hello_world_demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author  小尧
 * @date 2019-03-21 18:44:48
 */
@RestController
@RequestMapping("/")
public class HelloController {
    @GetMapping
    public String sayHello() {
        return "Hello SpringBoot！";
    }
}