N = int(input())
nums = list(map(int, input().split()))
dp = [10002 for i in range(N+1)]
dp[0] = 0
for i in range(N+1):
    for k, num in enumerate(nums,1):
        if i >= k :
            dp[i] = min(dp[i], dp[i - k] + num)
print(dp[-1])

