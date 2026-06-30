class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in range(0, n-1):
            res.append(max(arr[i+1:]))
        res.append(-1)
        return res
        