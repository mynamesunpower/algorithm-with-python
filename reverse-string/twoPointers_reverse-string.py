# 2개의 포인터를 이용해 범위를 조정해가면 풀이
def reverseString(s) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

str = ['h', 'e', 'l', 'l', 'o']
reverseString(str)
print(str)