class Solution:
    def reorderLogFiles(self,logs):
        letters = []
        digits = []
        for log in logs:
            if log.split()[1].isdecimal():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        print(letters + digits)


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    solution = Solution()
    solution.reorderLogFiles(logs)
