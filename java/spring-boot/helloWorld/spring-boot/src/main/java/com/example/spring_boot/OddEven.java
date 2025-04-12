package com.example.spring_boot;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class OddEven {

    @GetMapping("/odd-even")
    public EvenOddResponse checkEvenOdd(@RequestBody NumberRequest request) {
        int number = request.getNumber();
        String result = (number % 2) == 0 ? "even" : "odd";
        return new EvenOddResponse(number, result);
    }
}
