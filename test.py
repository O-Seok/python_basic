import unittest
from test_code import Stack


class CustomTests(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test(self):
        self.s.do_push(1)
        assert self.s.top() == 1

    def test_empty(self):
        assert self.s.do_empty() == 1
