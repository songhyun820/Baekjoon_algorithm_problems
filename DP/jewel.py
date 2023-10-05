num = int(input())

box = []
count = 0
a = 1
while True:
    input_arr = input()
    if input_arr == '0':
        break
    a,b = map(int, input_arr.split())
    box.append([a,b])
    count += 1

d = [1000000] * (num + 1)
d[0] = 0
for i in range(count):
    for j in range(box[i][1], num+1):
        if d[j - box[i][1]] != 1000000:
            d[j] = min(d[j], d[j - box[i][1]] + box[i][0])


if d[num] == 1000000 :
    print('fail')
else:
    print(d[num])