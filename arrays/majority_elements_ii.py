from collections import Counter

class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        counts = Counter(nums)
        result = []
        
        for num, freq in counts.items():
            if freq > n // 3:
                result.append(num)
        
        return result