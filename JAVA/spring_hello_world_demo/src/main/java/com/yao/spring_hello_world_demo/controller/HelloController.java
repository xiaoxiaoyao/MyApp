package com.yao.spring_hello_world_demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import reactor.core.publisher.Mono;

/**
 * @author  小尧
 * @date 2019-03-21 18:44:48
 */
@RestController
public class HelloController {
    @GetMapping("/")
    public String sayHello() {
        return "Hello SpringBoot！";
    }
    @GetMapping("/webflux")
    public Mono<String> SayHello() {
        return Mono.just("Welcome to reactive world ~");
    }
}