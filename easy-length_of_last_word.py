# beats 90.60% of solutions (both solutions ran 90.60%)

#solution 1---------------------------------

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1])
        

#solution 2---------------------------------
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        if len(s) == 0:
            return count
        for i in range(len(s) - 1, 0, -1):
            if s[i] == ' ' and count != 0:
                return count
            elif s[i] != ' ':
                count += 1
        
        if s[0] != ' ':
            return count + 1
        
        return count