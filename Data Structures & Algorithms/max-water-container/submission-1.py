class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_h = len(heights)
        areas = []
        for i in range(0, len_h-1):
            for j in range(i+1,len_h):
                area = min(heights[i], heights[j])*(j-i)
                areas.append(area)
        return max(areas)
        