# beats 98.86% of solutions

# solution 1--------------------------------------------------------------

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max_length = 0
        for i in range(len(strs)):
            if len(strs[i]) > max_length:
                max_length = len(strs[i])
        
        prefix = ""
        characters = []
        if max_length == 0:
            return prefix
        for i in range(max_length):
            try:
                char = strs[0][i]
            except:
                prefix = prefix.join(characters)
                return prefix

            try:
                for k in range(len(strs)):
                    if char == strs[k][i]:
                        continue
                    else:
                        prefix = prefix.join(characters)
                        return prefix
                characters.append(char)
            except:
                prefix = prefix.join(characters)
                return prefix
        prefix = prefix.join(characters)
        return prefix
    
# solution 2--------------------------------------------------------------
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest = 0
        index = 0
        ans = []
        prefix = ""
        for i in range(len(strs)):
            if len(strs[i]) > longest:
                longest = len(strs[i])
                index = i
        if longest == 0:
            return prefix
        for i in range(longest):
            letter = strs[index][i]
            for string in strs:
                try:
                    if string[i] != letter:
                        return prefix.join(ans)
                except:
                    return prefix.join(ans)
            ans.append(letter)
        return prefix.join(ans)
    
# solution 3--------------------------------------------------------------
# cut out the iteration bc i realized it must match every single word (so it applied to the first word)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        ans = []
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for string in strs:
                try:
                    if string[i] != letter:
                        return prefix.join(ans)
                except:
                    return prefix.join(ans)
            ans.append(letter)
        return prefix.join(ans)

# solution 4--------------------------------------------------------------
# can avoid checking every single one by sorting and 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return prefix
            prefix += first[i]
        return prefix 