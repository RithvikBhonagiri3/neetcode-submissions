class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_ar = 0
        areas = []
        num_ele = len(heights)
        for i,h in enumerate(heights):
            bar_ar = h
            areas.append(bar_ar)
            wid = 1
            if i >=1:
                for ele in heights[i-1::-1]:
                    if ele >= h:
                        wid = wid +1
                    else:
                        break
                areas.append(wid*h)
            if i < num_ele -1:
                for ele in heights[i+1:]:
                    if ele >=h:
                        wid = wid+1
                    else:
                        break
            areas.append(wid*h)
        return max(areas)






        