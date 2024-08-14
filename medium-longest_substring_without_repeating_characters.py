# beats 5% of solutions

# solution 1 (not very efficient)---------------------
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        largest = 0
        length = len(s)
        for i in range(length):
            seen = []
            count = 0
            for j in range(i, length):
                if s[j] in seen:
                    break
                else:
                    count += 1
                    seen.append(s[j])

            if count > largest:
                largest = count
        
        if count > largest:
            largest = count
        return largest

# solution 2---------------------------
            