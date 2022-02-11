class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x % 10 == 0 and x != 0):
            return False
        half = 0
        # by dividing by 10, we are removing the ones place and putting into the other half
        while(x > half):
            half = half * 10 + x % 10
            x = x//10
        return x == half or x == half//10