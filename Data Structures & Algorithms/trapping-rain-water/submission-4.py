class Solution:
    def trap(self, height: List[int]) -> int:
        def trim_edges(height):
            i = 0
            j = len(height)-1
            len_h = len(height)
            while height[i+1]>height[i] and i < len_h-2:
                i = i+1
            while height[j-1]>height[j] and j>2:
                j = j-1
            return height[i:j+1]
        #height = trim_edges(height)
        len_h = len(height)
        max_height = 0
        res = 0
        i = 1
        while i < len_h-1:
            max_height_left = max(height[:i])
            max_height_right = max(height[i+1:])
            max_water_height = min(max_height_left, max_height_right)
            res = res +max(0,max_water_height-height[i] )
            i = i+1
        return res






        