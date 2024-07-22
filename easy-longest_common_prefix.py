# beats 71.57% of solutions

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