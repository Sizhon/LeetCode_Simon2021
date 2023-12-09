class LongestSubstring.Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #constraint of being withint the ranges of a 32 bit integer
        if x <= -2**31 or x >= 2**31:
            return 0
        reverse = 0
        if x > 0:
            # for [::-1] this is the python slicing notation, which takes 3 arguments[start:stop:step]
            # if both start and stop is empty, it will iterate through entire string
            # [::1] would just return the string as it, it goes from beginning to end one step at a time
            # [::-1] returns a reversed string because it goes from end to beginning one step at a time(backwards)
            # more info at https://stackoverflow.com/questions/28535392/what-does-n-1-means-in-python
            reverse = int(str(x)[::-1])
        if x < 0:
            reverse = int(("-" + str(x * -1)[::-1]))
        # if the reversed int is bigger than the contraint of 32 bit int, it would also not be valid.
        if reverse <= -2**31 or reverse >= 2**31:
            return 0
        else:
            return reverse