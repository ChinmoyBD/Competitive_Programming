from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        arr = deque()
        arrCount = 0
        for i in s:
            if i not in arr:
                arr.append(i)
                arrCount += 1
                if maxCount < arrCount:
                    maxCount = arrCount
            else:
                while arrCount:
                    rm = arr.popleft()
                    arrCount -= 1
                    if rm == i:
                        break
                arr.append(i)
                arrCount += 1
                if maxCount < arrCount:
                    maxCount = arrCount
        return maxCount


ob = Solution()
print(ob.lengthOfLongestSubstring("pwwkew"))
