# -*- coding: UTF-8 -*-
n=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                n=n+1
                print(i,j,k)
print(n)