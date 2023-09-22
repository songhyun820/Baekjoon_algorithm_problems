n,k = map(int, input().split())
coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)
count = 0
for c in coins:
    count += k // c
    k %= c
print(count)