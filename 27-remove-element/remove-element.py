class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        occurance = 0
        for i in nums:
            if i!=val:
                nums[occurance]=i
                occurance+=1
        return occurance
        