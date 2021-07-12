str = ['h', 'e', 'l', 'l', 'o']
str.reverse()
print(str)

# 또 하나의 풀이.
# 나는 s = s[::-1] 이걸 생각했었는데[ 정상적으로 작동하지 않았음.
# 그 이유는, 슬라이싱의 공간 복잡도를 O(1)로 제한하다 보니 변수 할당을 처리하는데 제약이 있음.
# 그렇기에, 다음처럼 트릭을 사용하면 동작할 수 있음.
str[:] = str[::-1]
# 이거 다음에 한번 이용해볼 것