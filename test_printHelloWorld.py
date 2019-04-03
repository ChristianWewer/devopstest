import devopstest
from unittest import TestCase


class TestPrintHelloWorld(TestCase):
    def test_printHelloWorld(self):
        self.assertTrue(devopstest.printHelloWorld() == "Hello World!")
