class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique = set()

        for num in nums:
            if num in unique:
                return num
            else:
                unique.add(num)
        