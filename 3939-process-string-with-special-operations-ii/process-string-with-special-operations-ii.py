class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        n = len(s)

        lengths = [0] * n
        cur = 0

        for i, ch in enumerate(s):

            if 'a' <= ch <= 'z':
                cur += 1

            elif ch == '*':
                if cur > 0:
                    cur -= 1

            elif ch == '#':
                cur *= 2

            elif ch == '%':
                pass

            lengths[i] = cur

        if k >= cur:
            return '.'

        for i in range(n - 1, -1, -1):

            ch = s[i]

            prev_len = lengths[i - 1] if i > 0 else 0

            if 'a' <= ch <= 'z':

                if k == prev_len:
                    return ch

            elif ch == '#':

                k %= prev_len

            elif ch == '%':

                k = prev_len - 1 - k

            elif ch == '*':
                pass

        return '.'
        