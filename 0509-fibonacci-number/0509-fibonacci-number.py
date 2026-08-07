class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = [0,1]

        for i in range(2,n+1):
            ans = answer[i-1] + answer[i-2]
            answer.append(ans)
        return answer[n]
        