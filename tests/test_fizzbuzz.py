import pytest
import sys
import os
#test

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main  

def test_multiple_3():
    assert main.fizzbuzz(3) == "Fizz"
    assert main.fizzbuzz(6) == "Fizz"
    assert main.fizzbuzz(9) == "Fizz"

def test_multiple_5():
    assert main.fizzbuzz(5) == "Buzz"
    assert main.fizzbuzz(10) == "Buzz"
    assert main.fizzbuzz(20) == "Buzz"

def test_multiple_3_and_5():
    assert main.fizzbuzz(15) == "FizzBuzz"
    assert main.fizzbuzz(30) == "FizzBuzz"
    assert main.fizzbuzz(45) == "FizzBuzz"

def test_not_multiple_3_et_5():
    assert main.fizzbuzz(1) == 1
    assert main.fizzbuzz(2) == 2
    assert main.fizzbuzz(4) == 4
