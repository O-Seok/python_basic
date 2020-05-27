import unittest

class CustomTests(unittest, Test(Case)):
    def setUp(self):
        self.s = S()

    def test(self):
        self.s.push(1)
        assert self.s.top() == 1

    def test_empty(self):
        assert self.s.empty() == 1
