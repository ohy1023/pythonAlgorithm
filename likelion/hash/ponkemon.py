def solution(nums):
    hs = set()
    for num in nums:
        hs.add(num)
    if len(hs) < len(nums) // 2:
        return len(hs)
    else:
        return len(nums) // 2
