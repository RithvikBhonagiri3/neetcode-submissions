class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(0,len(temperatures)):
            if i < len(temperatures)-1:
                for j in range(0, len(temperatures[i+1:])):
                    resappen = 0
                    if temperatures[i]<temperatures[i+1:][j]:
                        resappen = j+1
                        break
                res.append(resappen)
            else:
                res.append(0)
        return res


        