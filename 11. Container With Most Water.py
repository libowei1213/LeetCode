class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        size = len(height)

        left = 0
        right = size - 1

        max = 0

        while left < right:
            vol = min(height[left], height[right]) * (right - left)
            if vol > max:
                max = vol

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max