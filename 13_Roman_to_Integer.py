class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        start = s[len(s) - 1]
        number = table.get(start)
        for i in range(len(s) - 2,-1,-1):
            if(table.get(s[i]) < table.get(start)):
                number = number - table.get(s[i])
                continue
            if table.get(s[i]) > table.get(start) or table.get(s[i]) == table.get(start):
                start = s[i]
                number = number + table.get(start)
        return number
                