package com.example.spring_boot;

public class EvenOddResponse {
    private int number;
    private String result;

    public EvenOddResponse(int number, String result) {
        this.number = number;
        this.result = result;
    }

    public int getNumber() {
        return number;
    }

    public String getResult() {
        return result;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public void setResult(String result) {
        this.result = result;
    }
}
