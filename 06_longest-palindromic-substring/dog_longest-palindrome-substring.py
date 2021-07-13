import re
# 가장 긴 팰린드롬 부분 문자열을 출력하라
def function(strs):
    if len(strs) > 1:
        a = 2
        for i in range(len(strs), 1, -1):
            for j in range(0, a):
                _strs = strs[j:j+i]
                if _strs == _strs[::-1]:
                    return _strs
            a += 1
    else:
        return strs


# runtime: 6512ms (21.07%)/ memory 14.2MB (82.48%)


c = function("a")
print(c)
