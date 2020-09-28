#!/usr/bin/env python3

def fibo(x):
    x_prev = x_prevv = 1
    print(x_prevv)
    print(x_prev)
    for i in range(x-2):
        tmp = x_prev
        x_prev += x_prevv
        x_prevv = tmp
        print(x_prev)

if __name__ == "__main__":
    fibo(15)
