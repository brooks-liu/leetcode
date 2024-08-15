# beats 86.52% of solutions

# solution 1---------------------------------------------
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n

# solution 2---------------------------------------------
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
            
        ans = 1

        while n != 0:
            if n % 2 != 0:
                ans *= x
            x *= x
            n = n / 2
        return ans