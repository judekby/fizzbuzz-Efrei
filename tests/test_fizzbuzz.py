import pytest
import sys
import os
#testtt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app  

def test_multiple_3():
    assert app.fizzbuzz(3) == "Fizz"
    assert app.fizzbuzz(6) == "Fizz"
    assert app.fizzbuzz(9) == "Fizz"

def test_multiple_5():
    assert app.fizzbuzz(5) == "Buzz"
    assert app.fizzbuzz(10) == "Buzz"
    assert app.fizzbuzz(20) == "Buzz"

def test_multiple_3_and_5():
    assert app.fizzbuzz(15) == "FizzBuzz"
    assert app.fizzbuzz(30) == "FizzBuzz"
    assert app.fizzbuzz(45) == "FizzBuzz"

def test_not_multiple_3_et_5():
    assert app.fizzbuzz(1) == 1
    assert app.fizzbuzz(2) == 2
    assert app.fizzbuzz(4) == 4