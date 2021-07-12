logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

letters, digits = [], []
for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)

# sort의 키 정렬. 키를 여러 개 이상 두는 경우 앞에서부터 차례대로 선순위 정렬을 한다.)
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(digits)
print(letters)
# 배열 + 배열은 합친 이후에 새로운 배열을 리턴.
result = letters + digits
print(result)