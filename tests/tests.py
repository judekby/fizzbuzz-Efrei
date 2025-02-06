import pytest
import main  

def multiple_3():
    assert main.fizzbuzz(3) == "Fizz"
    assert main.fizzbuzz(6) == "Fizz"
    assert main.fizzbuzz(9) == "Fizz"

def multiple_5():
    assert main.fizzbuzz(5) == "Buzz"
    assert main.fizzbuzz(10) == "Buzz"
    assert main.fizzbuzz(20) == "Buzz"

def multiple_3_and_5():
    assert main.fizzbuzz(15) == "FizzBuzz"
    assert main.fizzbuzz(30) == "FizzBuzz"
    assert main.fizzbuzz(45) == "FizzBuzz"

def not_multiple_3_et_5():
    assert main.fizzbuzz(1) == 1
    assert main.fizzbuzz(2) == 2
    assert main.fizzbuzz(4) == 4