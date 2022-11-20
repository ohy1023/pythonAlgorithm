# 가장 빠름
import re

class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


answer = Solution()

print(answer.isPalindrome("a car rac a"))
