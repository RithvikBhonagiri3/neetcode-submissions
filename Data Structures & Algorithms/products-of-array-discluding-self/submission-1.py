class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_prod = 1
        has_zero = 0
        length = 0
        res = []
        has_zero_idx = 0
        for num in nums:
            if num == 0:
                has_zero = has_zero+1
                has_zero_idx = int(length)
            else:
                non_zero_prod = non_zero_prod*num
            length = length+1
        if has_zero >1:
            return [0]*length
        elif has_zero == 1:
            res = [0]*length
            res[has_zero_idx] = non_zero_prod
            return res
        else:
            return [int(non_zero_prod/num) for num in nums]




        