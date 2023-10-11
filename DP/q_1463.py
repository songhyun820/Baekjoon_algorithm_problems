X = int(input())

dp = [0 for i in range(X+1)]
dp[0], dp[1] = 0, 0
for i in range(2,X+1):
    if i % 2 == 0 and i % 3 == 0 :
        dp[i] = min(dp[i - 1] + 1, dp[int(i/2)] + 1, dp[int(i/3)] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[int(i/2)] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[int(i/3)] + 1)
    else:
        dp[i] = dp[i-1] + 1
# print(dp)
# print([i for i in range(X+1)])
print(dp[-1])