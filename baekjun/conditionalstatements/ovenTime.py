hour, minute = map(int, input().split())
addMinute = int(input())

calMinute = minute + addMinute
if (calMinute) >= 60:
    addHour=calMinute // 60
    if hour + addHour > 23:
        hour = hour-24+addHour
    else:
        hour += addHour
    minute = calMinute % 60
else:
    minute += addMinute

print(hour,minute,sep=' ')
