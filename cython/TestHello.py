# -*- coding: utf-8 -*-
import pandas as pd
def hello1():
    data = pd.DataFrame()
    print('Life is short, I use Python.',data)


def hello2():
    print('666')
    print('Zen of Python')



def max(x, y):
    return x if x > y else y


if __name__ == '__main__':
    hello1()
    hello2()
    print(max(100, 99))