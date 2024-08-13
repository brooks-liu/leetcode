# beats 66.88% of solutions (solution 1), not the most space efficient so im trying to make that better
# solution 2 is much more space efficient, better than 95.82% of solutions

# solution 1----------------------------------------
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

        for i in range(1, length + 2):
            if numsLeft[i] == 1:
                return i


# solution 2---------------------------------------
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            spot = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[spot]:
                nums[i], nums[spot] = nums[spot], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
        