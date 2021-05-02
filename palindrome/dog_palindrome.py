import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == re.sub('[^a-z0-9]', '', s)


def isPalindrome(s: str) -> bool:
    s = re.sub('[^a-z0-9]', '', s.lower())
    return s == s[::-1]

result = isPalindrome("A Man, a plan, a canal: Panama")
print(result)

# runtime : 36ms
# memory usage : 15.7MB