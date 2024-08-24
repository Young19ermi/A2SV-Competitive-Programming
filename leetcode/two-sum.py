class Solution(object):
    def twoSum(self, nums, target):
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            currentsum = nums[left] + nums[right]
            if currentsum == target:
                return [left,right]
            elif currentsum < target:
                left+=1
            else:
                right-=1
          """
        seen = {}
        for i, num in enumerate(nums):
            if target-num in seen:
                return [seen[target - num], i]

            seen[num] = i    