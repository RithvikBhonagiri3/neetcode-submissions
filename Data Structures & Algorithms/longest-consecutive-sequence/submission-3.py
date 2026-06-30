class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)>0:
            res = 1
            temp_res = 1
            dist_nums = sorted(list(set(nums)))
            dist_nums_len = len(dist_nums)
            for idx in range(1,dist_nums_len):
                if dist_nums[idx]-dist_nums[idx-1] ==1:
                    temp_res = temp_res+1
                    if temp_res >res:
                        res = temp_res
                else:
                    temp_res = 1
            return res
        else:
            return 0
        