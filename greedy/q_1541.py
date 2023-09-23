import re
def find_int_sum(str):
    nums = re.findall(r'\d+',str)
    num = sum([int(num) for num in nums])
    return num

str = input()
if str.find('-') == -1:
    print(find_int_sum(str))
else:
    parts = str.split("-",1)
    num1 = find_int_sum(parts[0])
    num2 = find_int_sum(parts[1])
    print(num1-num2)