class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.split()
        if word:
             return len(word[-1])
        else:
             return 0