class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or needle == haystack:
            return 0
        trim = ""
        nlen = len(needle)
        for i in range(len(haystack) - nlen + 1):
            trim = haystack[i:i+nlen]
            if trim == needle:
                return i
        return -1