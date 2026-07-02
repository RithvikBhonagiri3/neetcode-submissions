class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_h = len(heights)
        res = 0
        l, r = 0, len_h-1
        while l <r:
            area = min(heights[l], heights[r])*(r-l)
            res = max(area, res)
            if heights[l]<heights[r]:
                l = l+1
            else:
                r = r-1
        return res

        