class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        m = len(matrix)  # 行数
        n = len(matrix[0])  # 列数

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid // n][mid % n] == target:
                return True
            elif target < matrix[mid // n][mid % n]:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    r = Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
    print(r)
