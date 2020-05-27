# 단위 테스트를 해본다.
# test_code.py 안의 Stack 클래스를 가져온다.
# Stack 클래스를 테스트 해본다!

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

if __name__ == '__main__':
    unittest.main()