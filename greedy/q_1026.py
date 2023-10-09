s = input()
str1 = list(map(int, input().split()))
str2 = list(map(int, input().split()))
str1.sort(reverse=True)
str2.sort()
result = 0
for a,b in enumerate(str1):
    result += b*str2[a]
print(result)
