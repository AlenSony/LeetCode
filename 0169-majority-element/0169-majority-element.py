class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique = set()
        result = nums[0]
        for num in nums:
            if num not in unique:
                unique.add(num)
                if nums.count(num) > nums.count(result):
                    result = num
        return result




        
        