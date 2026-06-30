class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0)+1
        num_dict=  dict(sorted(
        num_dict.items(), 
        key=lambda item: item[1],reverse = True))
        return list(num_dict.keys())[:k]