class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """

            
        l1 = [int(num) for num in str(n)]
        
        a = sum(l1)
        
        p = 1
        for num in l1:
            p *= num

        # Since n is positive, 'a' is at least 1, so (a + p) is never 0.
        return n % (a + p) == 0
       

        