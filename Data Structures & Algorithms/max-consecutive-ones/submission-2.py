class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        consec_max = 0
        for num in nums:
            if num:
                consec = consec +1
            else:
                if consec > consec_max:
                    consec_max = consec
                consec = 0
        return max(consec_max, consec)


        