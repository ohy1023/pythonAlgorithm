import sys
import time

start_time = time.time()
n = int(sys.stdin.readline())
cnt =0
ch = [0] * (n+1)
for i in range(2,n+1):
    if ch[i]==0:
        cnt +=1
        for j in range(i,n+1,i):
            ch[j] = 1
print(cnt)

end_time = time.time()
print("time : ",end_time-start_time)