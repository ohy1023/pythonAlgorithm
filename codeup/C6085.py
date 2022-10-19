w,h,b = map(int,input().split())

ans = (h*b*w)/(8 * 1024 * 1024)
print("%.2f MB"%ans)