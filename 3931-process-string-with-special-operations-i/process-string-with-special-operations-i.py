class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = ""

        for ch in s:

            if ch.isalpha():
                result += ch

            elif ch == '*':
                if result:
                    result = result[:-1]

            elif ch == '#':
                result += result

            elif ch == '%':
                result = result[::-1]

        return result