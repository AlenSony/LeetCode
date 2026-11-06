class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        series = [0, 1, 1]
        
        for i in range(0,n-2):
            series.append(sum(series[i:i+3]))
        
        return series[n]

        