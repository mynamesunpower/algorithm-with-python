import collections
from typing import Deque


def isPalindrome(self, s: str) -> bool:
    # 자료형 덱 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():  # isalnum은 영문자, 숫자 여부는 판별하는 함수.
            strs.append(char.lower())  # 대소문자를 구분하지 않으므로.

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    # 리스트의 pop(0)은 O(n)인데, 데크의 popleft()는 O(1)이다.
    # n번씩 반복하므로, 리스트 구현은 O(n^2), 데크 구현은 O(n)

    return True
