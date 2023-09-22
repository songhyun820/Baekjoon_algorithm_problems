N = int(input())
time = []
for i in range(N):
    Start,End = map(int, input().split())
    time.append((Start,End))
time.sort(key=lambda x :(x[1],x[0]))
count = 1
EndTime = time[0][1]
for ST,ET in time[1:]:
    if ST >= EndTime:
        EndTime = ET
        count +=1
print(count)