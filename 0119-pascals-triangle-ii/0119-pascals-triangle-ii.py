class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        answer = [[1], [1,1]]

        for i in range(2, rowIndex+1):
            current = [1]
            j = 0
            k = 1
            while k < len(answer[i-1]):
                current.append(answer[i-1][j]+answer[i-1][k])
                j+=1
                k+=1
            current.append(1)
            answer.append(current)
        return answer[rowIndex]
        