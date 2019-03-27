package com.yao.spring_hello_world_demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * 有时候属性太多了，一个个绑定到属性字段上太累，官方提倡绑定一个对象的bean，最后在Controller中引入ConfigBean使用即可，如下：
 */
@RestController
public class UserController2 {
    @Autowired
    ConfigBean configBean;

    @RequestMapping("/UserController2")
    public String hexo(){
        return configBean.getName()+configBean.getWant();
    }
}