class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximo = 0
        l, r = 0, len(heights) - 1
        while l < r:
            aux = min(heights[l], heights[r])
            curr = aux * abs(r - l)
            maximo = max(maximo, curr)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maximo