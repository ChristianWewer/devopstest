import devopstest
import pytest


def test_print_hello_world():
    assert devopstest.printHelloWorld() == "Hello World!"