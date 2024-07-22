# beats 86.26% of solutions

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # since we only have a limited number of cases it should be quite easy to brute force
        # keep track of number in an array, can get rid of this later
        numbers = []
        letters = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s)) :
            if i < len(s) - 1:
                if s[i] == 'I' and s[i+1] == 'V':
                    numbers.append(-1)
                    continue
                if s[i] == 'I' and s[i+1] == 'X':
                    numbers.append(-1)
                    continue
                if s[i] == 'X' and s[i+1] == 'L':
                    numbers.append(-10)
                    continue
                if s[i] == 'X' and s[i+1] == 'C':
                    numbers.append(-10)
                    continue
                if s[i] == 'C' and s[i+1] == 'D':
                    numbers.append(-100)
                    continue
                if s[i] == 'C' and s[i+1] == 'M':
                    numbers.append(-100)
                    continue
            numbers.append(letters[s[i]])
            #adds the number on
        
        return sum(numbers)