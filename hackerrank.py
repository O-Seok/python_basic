# 백중 1번 문
import sys

input=sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    # push method
    def do_push(self, number):
        return self.stack.append(number)

    # top method
    def do_top(self):
        if self.stack == []:
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    # size
    def do_size(self):
        return len(self.stack)

    # empty
    def do_empty(self):
        if self.stack == []:
            return 1
        else:
            return 0

    # pop
    def do_pop(self):
        if self.stack == []:
            return -1
        else:
            pop_num = self.stack[len(self.stack) - 1]
            del self.stack[len(self.stack) - 1]
            return pop_num


n = int(input())
stack = Stack()

for i in range(n):
    word = input().split()

    command = word[0]

    if command == 'push':
        stack.do_push(word[1])
    elif command == 'top':
        print(stack.do_top())
    elif command == 'size':
        print(stack.do_size())
    elif command == 'empty':
        print(stack.do_empty())
    elif command == 'pop':
        print(stack.do_pop())
    else:
        print('no command !')



