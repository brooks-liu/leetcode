# beats 72.16% of solutions

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
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        largest = 0
        length = len(s)
        characters = []
        if length == 0:
            return 0
        
        characters.append(s[left])
        while right < len(s) - 1:
            largest = max(right - left + 1, largest)

            right += 1
            if s[right] in characters:
                while characters.pop(0) != s[right]:
                    left += 1
                left += 1
                characters.append(s[right])
            else:
                characters.append(s[right])
        
        largest = max(right - left + 1, largest)

        return largest