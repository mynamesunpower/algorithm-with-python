str = '안녕하세요'

print(str[1:4])  # 녕하세 (1부터 4 이전까지)
print(str[1:-2])  # 녕하 (1부터 -2 이전까지)
print(str[1:])  # 녕하세요
print(str[:])  # 안녕하세요 -> 사본을 리턴. (값을 복사)
print(str[1:100])  # 에러? X 문자열의 최대 길이까지 표현. // 녕하세요랑 동일
print(str[-1])  # 요
print(str[-4])  # 녕
print(str[:-3])  # 안녕
print(str[-3:])  # 하세요
print(str[::1])  # 안녕하세요
print(str[::-1])  # 요세하녕안
print(str[::2])  # 안하요