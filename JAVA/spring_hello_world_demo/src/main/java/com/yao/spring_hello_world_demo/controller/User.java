package com.yao.spring_hello_world_demo.controller;
/**
 *     private Long id;
 *     private String name;
 *     private Integer age;
 */
public class User {
 
    private Long id;
    private String name;
    private Integer age;

    // 一堆setter和getter 

    /**
     * @return the id
     */
    public Long getId() {
        return id;
    }

    /**
     * @return the age
     */
    public Integer getAge() {
        return age;
    }

    /**
     * @param age the age to set
     */
    public void setAge(Integer age) {
        this.age = age;
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
     * @param id the id to set
     */
    public void setId(Long id) {
        this.id = id;
    }
 
     
}