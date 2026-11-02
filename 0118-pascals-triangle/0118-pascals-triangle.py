class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        answer = [[1], [1,1]]

        for i in range(2, numRows):
            current = [1]
            j = 0
            k = 1
            while k < len(answer[i-1]):
                current.append(answer[i-1][j]+answer[i-1][k])
                j+=1
                k+=1
            current.append(1)
            answer.append(current)
        return answer
    

        
        