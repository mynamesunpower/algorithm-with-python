
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():  # isalnum은 영문자, 숫자 여부는 판별하는 함수.
            strs.append(char.lower())  # 대소문자를 구분하지 않으므로.

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
