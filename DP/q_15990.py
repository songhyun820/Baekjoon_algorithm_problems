#입력
T = int(input())
nums = []
for _ in range(T):
    nums.append(int(input()))

#연산
max_num = max(nums)
dp = [[0 for _ in range(3)] for _ in range(max_num+1)]
dp[0], dp[1], dp[2], dp[3] = [0,0,0], [1,0,0],[0,1,0], [1,1,1]
for i in range(4, max_num+1):
    dp[i][0], dp[i][1], dp[i][2] = dp[i-1][1]+dp[i-1][2], dp[i-2][0]+dp[i-2][2], dp[i-3][0]+dp[i-3][1]

#출력
result = ""
for i in nums:
    result += str(sum(dp[i]) % 1000000009) +'\n'
print(result[:-1])
