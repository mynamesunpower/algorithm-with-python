# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 아늫으며 구두점 도한 무시한다.
import collections, re

paragraph = "bob hit a ball, the hit ball flew far after it was hit."
paragraph = re.sub('[^a-z ]', ' ', paragraph.lower())
print(f'paragraph: {paragraph}')
banned = ["hit"]

countered = collections.Counter(paragraph.split())
print(f'countered: {countered}')
for ban_item in banned:
    if ban_item in countered:
        countered.pop(ban_item)

print(countered.most_common(1)[0][0])

# solved!
# runtime: 24ms (98.94%)
# memory usage: 14.4MB (22.87%)