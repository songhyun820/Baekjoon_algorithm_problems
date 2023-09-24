N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()
total =0
while length:
    min_price = min(price)
    min_price_index = price.index(min_price)
    total += sum(length[min_price_index:]) * min_price
    price = price[:min_price_index]
    length = length[:min_price_index]
print(total)


# N = int(input())
# length = list(map(int, input().split()))
# price = list(map(int, input().split()))
# total = 0
# m = price[0]
# for i in range(N-1):
#     if price[i] < m:
#         m = price[i]
#     total += m*length[i]
# print(total)