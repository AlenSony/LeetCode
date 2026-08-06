class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] not in num_set:
                num_set.add(nums[i])
                result.append(nums[i])
            else:
                result.remove(nums[i])
        return result[0]
        
        
        


