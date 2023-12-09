class LongestSubstring.Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #have a dict
        dict = {}
        #iterates throught nums list once
        for i in range(len(nums)):
            # if current index's pair is in dict, it will return
            pair = target - nums[i]
            if pair in dict:
                """ because the lower index will never see values in the higher index, it will only ever return once it found
                the pair it was initially looking for further down the line. Given [2,7,11,15], when i is 0, it doesnt return
                because 7 is not in the dict. When i is 1, it is looking for 2 which was added before."""
                return [dict.get(pair), i]
            dict[nums[i]] = i