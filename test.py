# 단위 테스트를 해본다.
# test_code.py 안의 Stack 클래스를 가져온다.
# Stack 클래스를 테스트 해본다!

# unittest = https://docs.python.org/ko/3/library/unittest.html
# assert method = https://docs.python.org/ko/3/library/unittest.html#assert-methods

import unittest
from test_code import Stack

def a(b, c):
    return b + c

class CustomTests(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_top(self):
        self.s.do_push(1)
        assert self.s.do_top() == 1

    def test_empty(self):
        assert self.s.do_empty() == 1

    def test_pop(self):
        # self.s.do_push(3)
        assert self.s.do_pop() == -1

    def test_pop_assertEqual(self):

        # self.s.do_pop() 결과값이 -1 과 같은?
        self.assertEqual(self.s.do_pop(), -1)
        # self.s.do_pop() 결과가 None이 아닌가?
        self.assertIsNotNone(self.s.do_pop())

# Unittest를 위해 아래를 작성해줘야 한다.
if __name__ == '__main__':
    unittest.main()