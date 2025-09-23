# import math as m
from math import pi

def circle(r):
    return pi * r * r


if __name__ == '__main__':
    r = input("Enter radius: ")
    print(f"반지름이 {r}인 원의 넓이 :  {circle(int(r))}")