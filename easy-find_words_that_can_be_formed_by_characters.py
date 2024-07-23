# beats 96.64% of solutions

# solution 1--------------------------------------------------
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        sum = 0
        for i in range(len(words)):
            counter = 0
            characters = [c for c in chars]
            for j in range(len(words[i])):
                if words[i][j] in characters:
                    counter += 1
                    ind = characters.index(words[i][j])
                    characters[ind] = ""
                else:
                    continue
            if counter == len(words[i]):
                sum += counter
        return sum


# solution 2--------------------------------------------------
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        letters = {}
        score = 0
        for letter in chars:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        for word in words:
            temp = letters.copy()
            good = True
            for letter in word:
                if letter not in temp:
                    good = False
                    break
                temp[letter] -= 1
                if temp[letter] < 0:
                    good = False
                    break
            if good:
                score += len(word)

        return score


if __name__ == "__main__":
    test = ["cat","bt","hat","tree"]
    chars = "atach"
    solution = Solution()
    print(solution.countCharacters(test, chars))
        
#solution 3-----------------------------------------------------------------

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        letters = [0] * 26
        score = 0
        for letter in chars:
            letters[ord(letter) - ord('a')] += 1
        for word in words:
            if self.canForm(word, letters):
                score += len(word)
        return score
    
    def canForm(self, word, letters):
        needed = [0] * 26

        for letter in word:
            index = ord(letter) - ord('a')
            needed[index] += 1
            if needed[index] > letters[index]:
                return False
        return True


        