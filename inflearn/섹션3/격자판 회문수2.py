def isSame(nums):
    if all(nums[k] == nums[4-k] for k in range(2)):
        return True
    return False

a = [list(map(int,input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        if isSame(a[i][j:j+5]):
            cnt+=1
        if isSame(list(zip(*a[j:j+5]))[i]):
            cnt+=1
print(cnt)




