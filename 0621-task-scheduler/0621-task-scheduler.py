from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        freq = list(Counter(tasks).values())
        maxF = max(freq)
        cnt = freq.count(maxF)
        return max(len(tasks), (maxF - 1) * (n + 1) + cnt)