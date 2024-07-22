# solution 2 somehow only around 20% of the runtime of solution 1, despite being O(n^2) still
# beats 89.45% of solutions


# solution 1--------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# solution 2--------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in nums and nums.index(compliment) != i:
                return [nums.index(compliment), i]


# solution 3--------------------------------------------------------
# tried using the fact that dictionaries are o(1) look up
class Solution(object):
    def twoSum(self, nums, target):
        pairs = {}
        for i in range(len(nums)):
            pairs[nums[i]] = i
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in pairs.keys() and pairs[compliment] != i:
                return [i, pairs[compliment]]       

#solution 4------------------------------------------------------------
# had to look at the solutions and saw that they just iterate in one loop instead of two
class Solution(object):
    def twoSum(self, nums, target):
        pairs = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in pairs:
                return [i, pairs[compliment]]       
            pairs[nums[i]] = i 

