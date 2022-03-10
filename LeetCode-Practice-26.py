class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        i = 0
        while i < len(nums)-1:
            if i+1 <= len(nums)-1 and nums[i] == nums[i+1]:
                nums.pop(i+1)
                
            else:
                i += 1
            count += 1
        return count
                
