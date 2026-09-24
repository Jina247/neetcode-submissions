class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Step 1: Calculate exclusive prefix product directly into result array
        # res[i] will contain the product of all elements to the left of i
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
            
        # Step 2: Multiply by suffix product on the fly moving backward
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix  # Prefix * Suffix
            suffix *= nums[i] # Update suffix for the next element to the left
            
        return res
