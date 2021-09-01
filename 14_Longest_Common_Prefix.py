class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if strs is empty or strs[0] is empty, it will return ""
        if ((not strs) or len(strs) == 0 or (not strs[0])):
            return ""
        
        # iterate through the length of first word
        for j in range(len(strs[0])):
            # character at index j of first word
            c = strs[0][j]
            # iterate through the words in strs
            for i in range(len(strs)):
                # check if letter is equal to a word at the same index
                # or if the current index is the last letter of a word
                if (j == len(strs[i]) or strs[i][j] != c):
                    # returns the prefix as a substring of the first word j doesn't include the current letter
                    # because range of :j is always 1 less than j
                    return strs[0][:j]
        return strs[0]