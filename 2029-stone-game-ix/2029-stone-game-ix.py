class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        cnt = [0, 0, 0]
        for x in stones:
            cnt[x % 3] += 1
            
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]
        
        # If no 1s or 2s are available, Alice cannot even make a valid first move
        if c1 == 0 and c2 == 0:
            return False

        # When c0 is even, c0 does not change turn parity
        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0
        else:
            # When c0 is odd, it flips the winning advantage
            return abs(c1 - c2) > 2
        