class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        dupe = []

        for num in nums:
            if num in result or num in dupe:
                result.remove(num)
                dupe.append(num)
            else:
                result.append(num)
        return result[0]

        