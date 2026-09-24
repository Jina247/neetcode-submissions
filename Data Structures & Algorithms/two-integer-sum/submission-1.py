class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        output = []
        for i in range(0, n):
            x = target - nums[i]
            if x in nums[i+1:]:
                j = nums.index(x, i + 1)
                output.append(i)
                output.append(j)
                return output