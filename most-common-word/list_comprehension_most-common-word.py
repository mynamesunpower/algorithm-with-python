import collections
import re

paragraph = "bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
         .lower().split()
         if word not in banned]

counts = collections.Counter(words)
print(counts.most_common(1)[0][0])

# runtime: 36ms (62.76%)
# memory usage: 14.6MB (22.87%)
# 신기하당
