class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        helper = []
        for i,t in enumerate(temperatures):
            while helper and t > helper[-1][0]:
                helpert,helperi = helper.pop()
                res[helperi] = i - helperi
            helper.append([t,i])
        return res


        