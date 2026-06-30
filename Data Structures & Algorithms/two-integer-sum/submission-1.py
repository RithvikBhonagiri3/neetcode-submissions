class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        le = len(nums)
        for idx in range(0, le):
            for id2 in range(idx+1,le):
                if nums[id2]==target-nums[idx]:
                    return [idx,id2]
        