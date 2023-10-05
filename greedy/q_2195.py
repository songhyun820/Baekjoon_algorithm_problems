import sys

def find_all_indices(input_string, target_character):
    indices = []
    for index, char in enumerate(input_string):
        if char == target_character:
            indices.append(index)
    return indices

str1 = input()
str2 = input()
i = 0
result = 0
while i < len(str2):
    index_set = find_all_indices(str1, str2[i])
    count_set = []
    for j in index_set:
        k = 0
        while j+k < len(str1) and i+k < len(str2) and str1[j + k] == str2[i + k]:
            k += 1
        count_set.append(k)
    i += max(count_set)
    count_set.clear()
    result +=1
print(result)
