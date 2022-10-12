T = int(input())
for i in range(T):
    N,s,e,k = map(int,input().split())
    arr = list(map(int,input().split()))
    result = arr[s-1:e]
    result.sort()
    print("#{0} {1}".format(i+1,result[k-1]))

