class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        result = []
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        sorted_dict = dict(sorted(my_dict.items(),key=lambda item: item[1], reverse=True))
            
        for key in sorted_dict:
            result.append(key)
            if len(result) == k:
                return result

        