class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaner = ""
        for ch in s:
            if ch.isalnum():
                cleaner+=ch.lower()
        return cleaner == cleaner[::-1]
