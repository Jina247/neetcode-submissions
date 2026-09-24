class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = 1
        right_product = 1
        output = [1] * n

        for i in range (len(nums)):
            output[i] = left_product
            left_product = left_product * nums[i]
        for i in range (len(nums) - 1, -1, -1):
            output[i] *= right_product
            right_product = right_product * nums[i]
            
        return output
