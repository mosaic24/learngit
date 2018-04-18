#!/usr/bin/python
# -*- coding: UTF-8 -*-
#质数分解
from sys import stdout
from math import sqrt
n = int(input("input number:\n"))
print("n = %d" % n)
n1=int(sqrt(n+1))
for i in range(2,n1):
    while i!= n1:
        if n % i == 0:
            stdout.write(str(i))
            stdout.write("*")
            n = n / i
        else:
            break
print("%d" % n)