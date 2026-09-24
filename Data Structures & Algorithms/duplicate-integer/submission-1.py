class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for num in nums:
            seen.add(num)
        if len(seen) == n:
            return False
        else:
            return True