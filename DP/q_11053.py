import copy

def find_longest_length_2d_array(arr):
    max_length = 0
    result = arr[0]
    for sub_array in arr:
        length = len(sub_array)
        if length > max_length:
            max_length = length
            result = sub_array
    return str(max_length) + "\n" + str(result)[1:-1]

n = int(input())
ary = list(map(int, input().split()))
dp = [[ary[0]]]
tmp2 = []
for i in range(1,n):
    if ary[i-1] < ary[i]:
        for j in dp:
            if j[-1] < ary[i]:
               j.append(ary[i])
    elif ary[i-1] > ary[i]:
        tmp = copy.deepcopy(dp)
        while tmp[0][-1] >= ary[i] :
                tmp[0].pop()
                if not tmp[0]:
                    break
        tmp[0].append(ary[i])
        tmp2.clear()
        tmp2.append(tmp[0])
        max_len = len(tmp[0])
        if len(dp) > 1 :
            for k in tmp[1:]:
                while k[-1] >= ary[i] :
                    k.pop()
                    if not k:
                        break
                k.append(ary[i])
                if len(k) > max_len :
                    tmp2.clear()
                    tmp2.append(k)
                elif len(k) == max_len:
                    tmp2.append(k)
        for l in tmp2:
            dp.append(l)
    else:
        continue
print(find_longest_length_2d_array(dp))