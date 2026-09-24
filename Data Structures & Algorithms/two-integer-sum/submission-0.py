class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        output = []
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)

        return output
                    