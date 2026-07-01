class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement =  defaultdict(int)
        id1 = 1
        for num in numbers:
            if complement[num]:
                return [complement[num], id1 ]

            complement[target-num]= id1
            id1 +=1


        