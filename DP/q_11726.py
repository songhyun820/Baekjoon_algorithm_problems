n = int(input())
if n == 1 :
    print(1)
else:
    dp = [0 for i in range(n+1)]
    dp[0], dp[1], dp[2] = 0, 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n] % 10007)
