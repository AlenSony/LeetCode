class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        number = int("".join(map(str, digits)))

        number += 1

        result = [int(d) for d in str(number)]
        
        return result