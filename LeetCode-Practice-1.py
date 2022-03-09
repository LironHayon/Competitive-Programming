class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            if target - nums[i] in nums:
                index = nums.index(target - nums[i])
                if index != i:
                    return i,index
            
            
            
            
            
            

# Runtime: 600 ms, faster than 48.45% of Python online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 70.57% of Python online submissions for Two Sum.
