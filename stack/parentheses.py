#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : parentheses.py
@Time : 4/17/22 3:41 PM
@Desc: 
"""


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        return data

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0


def balance_check(expression):
    if len(expression) % 2 != 0:
        return False
    opening_brackets = set('([{')
    pairs = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = Stack()

    for bracket in expression:
        if bracket in opening_brackets:
            stack.push(bracket)
        else:
            popped_bracket = stack.pop()
            if (popped_bracket, bracket) not in pairs:
                return False
    return stack.is_empty()


def main():
    if balance_check('[{}]([])'):
        print("Balanced")
    else:
        print("Not Balanced")

    if balance_check('{[}]([])'):
        print("Balanced")
    else:
        print("Not Balanced")


if __name__ == '__main__':
    main()
