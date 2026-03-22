package com.yao.spring_hello_world_demo.controller;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.reactive.WebFluxTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.reactive.server.WebTestClient;

@RunWith(SpringRunner.class)
@WebFluxTest(controllers = HelloController.class)
public class HelloTests {
    @Autowired
    WebTestClient client;

    @Test
    public void getSayHello() {
        client.get().uri("/webflux").exchange().expectStatus().isOk();
    }
}