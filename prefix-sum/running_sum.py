class Solution:
    def runningSum(self, nums):
        result = []
        running_total = 0
        
        for num in nums:
            running_total += num
            result.append(running_total)
        
        return result