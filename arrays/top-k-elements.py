
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        d=Counter(nums)
        buckets=[[]for i in range(len(nums)+1)]
        for key,freq in d.items():
            buckets[freq].append(key)
        result = []
        for i in range(len(buckets)-1,0,-1):
            for key in buckets[i]:
               result.append(key)
               if len(result)==k:
                  return result
