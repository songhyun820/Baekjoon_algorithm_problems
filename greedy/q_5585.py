money = int(input())
money_arr = [500, 100, 50, 10, 5, 1]
money = 1000 - money
count = 0
for i in money_arr:
    count += money//int(i)
    money %= int(i)
print(count)
