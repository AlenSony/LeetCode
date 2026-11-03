class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = [[]]

        for num in nums:

            new_subset = []

            for subset in answer:
                new_subset.append(subset+[num])

            answer.extend(new_subset)
        return answer
        
        

        