T = int(input())
nums = []
for _ in range(T):
    nums.append(int(input()))
max_num = max(nums)
dp = [0 for i in range(max_num+1)]
dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 4
for i in range(4, max_num+1):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
for k in nums:
    print(dp[k])

