package com.example.spring_boot;

public class NumberRequest {
    private int number;

    public NumberRequest(int number) {
        this.number = number;
    }

    public int getNumber() {
        return number;
    }

    public int setNumber(int number) {
        return this.number = number;
    }
}
