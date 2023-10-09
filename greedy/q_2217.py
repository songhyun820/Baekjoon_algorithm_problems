
N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    arr.append(x)
#   rope_list = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
temp = arr[0]
result = arr[0]
for i,weight in enumerate(arr[1:], start=2):
    temp2 = i*weight
    if temp2 >= result :
        result = temp2
print(result)
