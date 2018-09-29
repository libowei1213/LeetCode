class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_left = []
        for i in range(len(height)):
            if i == 0:
                max_left.append(height[i])
            else:
                max_left.append(max(max_left[-1], height[i]))

        max_right = []
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                max_right.insert(0, height[i])
            else:
                max_right.insert(0, max(max_right[0], height[i]))

        area = 0
        for i in range(1, len(height) - 1):
            min_max = min(max_left[i - 1], max_right[i + 1])
            if min_max > height[i]:
                area += (min_max - height[i])
        return area


if __name__ == '__main__':
    r = Solution().trap([5, 1, 2, 1, 5])
    print(r)
