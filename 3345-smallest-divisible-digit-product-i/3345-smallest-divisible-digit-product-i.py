class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        flag = 1
        while flag:
            num = str(n)
            digitProduct = 1
            for c in num:
                digitProduct *= int(c)
            if digitProduct % t == 0:
                return int(n)
                break
            else:
                n += 1

        
