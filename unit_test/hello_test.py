from test import hello
import pytest

def test_hello():
   assert hello("Abhishek") == "hello,Abhishek"

def test_argument():
      for name in ["Abhishek","Tudu","Malu"]:
         assert hello(name) == f"hello,{name}"

