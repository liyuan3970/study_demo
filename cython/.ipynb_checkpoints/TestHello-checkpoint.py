# -*- coding: utf-8 -*-

def hello1():
    print('Life is short, I use Python.')


def hello2():
    print('666')
    print('Zen of Python')



def max(x, y):
    return x if x > y else y


if __name__ == '__main__':
    hello1()
    hello2()
    print(max(100, 99))