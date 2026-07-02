class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mp = {}
        l = len(nums)
        res = []
        nums = sorted(nums)
        for i in range(0,l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = l-1
            while j < k:
                if -nums[i] > nums[j]+nums[k]:
                    j = j +1
                elif -nums[i] < nums[j]+nums[k]:
                    k = k-1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        return res