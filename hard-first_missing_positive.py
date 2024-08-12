# beats 65.75% of solutions

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        numsLeft = {}
        if length == 0:
            return 1
        if length == 1:
            if nums[0] == 1:
                return 2
            return 1

        for i in range(1, length + 2):
            numsLeft[i] = 1
        
        for i in range(length):
            if nums[i] in numsLeft:
                numsLeft[nums[i]] = 0
            else:
                continue
        
        for i in range(1, length + 2):
            if numsLeft[i] == 1:
                return i
            


        

        
        
        