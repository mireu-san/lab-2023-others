package com.example.demo.rest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestRestController {
    // expose "/" as routing to main and so return test message.

    @GetMapping("/")
    public String testMessage() {
        return "This is test. Run by Java Spring";
    }

    @GetMapping("/workout")
    public String getDailyWorkout() {
        return "printed by getDailyWorkout, public String.";
    }

    @GetMapping("/fortune")
    public String getDailyFortune() {
        return "Today is lucky day";
    }
}
