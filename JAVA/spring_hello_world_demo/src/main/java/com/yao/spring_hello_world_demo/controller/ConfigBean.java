package com.yao.spring_hello_world_demo.controller;

import org.springframework.boot.context.properties.ConfigurationProperties;

/**
 * 有时候属性太多了，一个个绑定到属性字段上太累，官方提倡绑定一个对象的bean，这里我们建一个ConfigBean.java类，顶部需要使用注解@ConfigurationProperties(prefix
 * = “com.yao”)来指明使用哪个
 * 
 */
@ConfigurationProperties(prefix = "com.yao")
public class ConfigBean {
    private String name;
    private String want;

    /**
     * @return the want
     */
    public String getWant() {
        return want;
    }

    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @param want the want to set
     */
    public void setWant(String want) {
        this.want = want;
    }
}