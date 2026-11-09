class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        rows = len(matrix)
        columns = len(matrix[0])

        output = [[] for _ in range(columns) ]

        for i in range(rows):
            for j in range(columns):
                output[j].append(matrix[i][j])
        return output

        