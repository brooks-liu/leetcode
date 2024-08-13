# beats 92.26% of solutions

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        i = len(digits) - 1
        while i > 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits
        if digits[0] == 9:
            digits[0] = 0
            newlist = [1]
            newlist.extend(digits)
            return newlist
        else:
            digits[0] += 1
            return digits
