class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = []
        id1 = 1
        for num in numbers:
            complement_idx = 1
            for num2 in complement:
                if num==num2:
                    return [complement_idx, id1]
                else :
                    complement_idx = complement_idx+1
            complement.append(target-num)
            id1 +=1


        