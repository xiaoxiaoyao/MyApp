package com.yao.spring_hello_world_demo.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * 
 * application.properties提供自定义属性的支持，这样我们就可以把一些常量配置在这里：全局配置文件application.properties，放在src/main/resources目录下或者类路径的/config下。
 * 然后直接在要使用的地方通过注解@Value(value=”${config.name}”)就可以绑定到你想要的属性上面
 */
@RestController
public class UserController {

    @Value("${com.yao.name}")
    private String name;
    @Value("${com.yao.want}")
    private String want;
    @Value("${com.yao.address}")
    private String address;

    @RequestMapping("/UserController")
    public String hexo() {
        return name + " , " + want + " , " + address;
    }

}