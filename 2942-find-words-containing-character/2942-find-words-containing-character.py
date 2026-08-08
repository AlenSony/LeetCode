class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

        result = []
        i = 0

        for word in words:
            if x in word:
                result.append(i)
            i += 1
        return result
        