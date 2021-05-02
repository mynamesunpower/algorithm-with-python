import collections

a = dict()
b = {}
c = {
    'key1': 'value1',
    'key2': 'value2'
}
print(c)
print(c['key1'])
c['key3'] = 'value3'
# print(c['key4']) KeyError
# try catch 구문으로 예외 처리 가능하다
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키입니다')

for key, value in c.items():
    print(key, value)

del c['key3']

print(c)

# defaultdict 객체
default = collections.defaultdict(int)
default['A'] = 5
default['B'] = 4
print(default)

default['C'] += 1
print(default)

# Counter 객체
cc = [1, 2, 3, 4, 5, 5, 5, 6, 6]
counter = collections.Counter(cc)
print(counter)
print(type(counter))
print(counter.most_common(2))