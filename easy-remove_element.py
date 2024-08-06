# beats 80.14% of solutions


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                continue
            count += 1
            i += 1
        return count
            
        