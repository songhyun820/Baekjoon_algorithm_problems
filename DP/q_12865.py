# N, K = map(int, input().split())
# objects = []
# for _ in range(N):
#     objects.append(list(map(int, input().split())))

# values = [-1] * (K+1)
# values[0] = 0
# for i in range (N):
#     w = objects[i][0]
#     v = objects[i][1]

#     for j in range(w,K+1):
#         if values[j-w] != -1:
#             values[j] = max(values[j], values[j-w]+v)
#             print(values, objects[i][0], objects[i][1])
# print(max(values))

# N, K = map(int, input().split())
# objects = [[0,0]]
# knapsack = [[0 for _ in range(K +1)] for _ in range(N + 1)]
# for _ in range(N):
#     objects.append(list(map(int, input().split())))

# for i in range (1,N+1):
#     w = objects[i][0]
#     v = objects[i][1]

#     for j in range(1,K+1):
#         if j < w :
#             knapsack[i][j] = knapsack[i-1][j]
#         else:
#             knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-w]+v)
# print(knapsack[N][K])
from sys import stdin
input = stdin.readline

N, K = map(int,input().split())

juels=[None for i in range(N)]
dp = [0 for i in range(K+1)]

for i in range(N):
    juels[i]=tuple(map(int,input().split()))

juels.sort()
for i in range(N):
    w, v = juels[i]
    j=K-w
    while j>=0:
        dp[j+w]=max(dp[j]+v,dp[j+w])
        print(dp, w, v)
        j-=1

print(dp[K])


