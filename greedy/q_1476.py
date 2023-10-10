import sys

E,S,M = map(int, sys.stdin.readline().split())
E, S, M = E-1, S-1, M-1
x = 0
while (E+x)%28 != S:
    x += 15
    if(x > 10000) :
        break
while (E+x)%19 != M:
    x += 420

print(E+x+1)   

#조건 1개씩 ㄱㄱ