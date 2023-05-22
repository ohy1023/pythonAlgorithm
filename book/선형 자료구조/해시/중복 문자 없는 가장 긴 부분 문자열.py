# 슬라이딩 윈도우 + 투 포인터
def solution_sliding_window_two_pointer(s: str) -> int:
    used = {}
    max_length = start = 0
    for idx, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, idx - start + 1)

        used[char] = idx

    return max_length


if __name__ == "__main__":
    print(solution_sliding_window_two_pointer("pwwkew"))
