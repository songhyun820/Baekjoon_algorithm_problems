N = int(input())
nums = list(map(int, input().rstrip().split()))
dp = [0 for i in range(N+1)]
for i in range(N+1):
    for k, num in enumerate(nums,1):
        if i >= k :
            dp[i] = max(dp[i], dp[i - k] + num)
print(dp[-1])

