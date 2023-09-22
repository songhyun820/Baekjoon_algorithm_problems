N = int(input())
arr = list(map(int, input().split()))
arr.sort()
time =  0
for i in range(N+1):
    time += sum(arr[:i])
    print(time)
print(time)
