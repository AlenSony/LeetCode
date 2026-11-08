class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        jumps = 0
        current = 0
        longest = 0

        for i in range(n-1):

            longest = max(longest, i + nums[i])

            if i == current:
                jumps += 1
                current = longest
        return jumps