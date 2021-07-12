
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

# 출력
# [
#   ['ate', 'eat', 'tea']
#   ['nat', 'tan']
#   ['bat']
# ]

# 실패
# Time Limit Exceeded -> 111/114 test cases passed
# 원인 -> 불필요한 반복문의 사용으로 length가 긴 테스트 케이스로 시간제한에 걸렸다.

# _input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
_input = ["", ""]


def groupAnagrams(strs):
    if len(strs) <= 1:
        return [strs]
    res_arr = []
    for i in range(0, len(strs)):
        flag = True
        for ary in res_arr:
            if strs[i] in ary:
                flag = False
                continue
        if not flag:
            continue
        arr = [strs[i]]
        for j in range(i, len(strs)):
            if i == j:
                continue
            if sorted(strs[i]) == sorted(strs[j]):
                arr.append(strs[j])
                if strs[i] not in arr:
                    arr.append(strs[i])
        res_arr.append(arr)
    return res_arr


dd = groupAnagrams(_input)
print(dd)
