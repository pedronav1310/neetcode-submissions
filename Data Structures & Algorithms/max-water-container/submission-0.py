class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_height = 0
        while right > left:
            height = min(heights[left], heights[right])
            actual = (right-left)*height
            if heights[right] > heights[left]:
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                left+=1
                right-=1
            max_height = max(max_height, actual)
        return max_height