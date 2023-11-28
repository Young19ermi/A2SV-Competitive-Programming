class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefixsum = [1] * n

        for i in range(1,n):
            prefixsum[i] = prefixsum[i-1] * nums[i-1] #we already state how this works --> exclusive prefix sum
            
        rightproduct = 1
        for i in range(n-1, -1 ,-1):
            prefixsum[i] *= rightproduct
            
            rightproduct *= nums[i]
        return prefixsum    