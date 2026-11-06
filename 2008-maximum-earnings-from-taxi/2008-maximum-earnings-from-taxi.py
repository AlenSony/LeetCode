class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """

        ending_at = [[] for _ in range(n+1)]

        for start, stop, tip in rides:
            ending_at[stop].append((start, tip))

        dp = [0]*(n+1)

        for i in range(1, n+1):

            dp[i] = dp[i-1]

            for start, tip in ending_at[i]:

                profit = i - start + tip

                dp[i] = max(dp[i], dp[start] + profit)

        return dp[n]




        