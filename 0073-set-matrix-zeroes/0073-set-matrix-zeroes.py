class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row = set()
        column = set()

        m = len(matrix)

        n = len(matrix[0])

        for i in range(0, m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)

        for i in range(0, m):
            if i in row:
                matrix[i] = [0]*n
        
        for j in range(0,n):
            if j in column:
                for i in range(0,m):
                    matrix[i][j] = 0
        
                    
        