class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i, b in enumerate(num2[::-1]):
            for j, a in enumerate(num1[::-1]):
                # 被乘数 j 进位
                # 乘数   i 进位

                temp = int(a) * int(b)

                # 两数相乘，加在相应的进位上
                result[i + j] += temp

        for i in range(len(result) - 2):
            add = result[i] // 10
            left = result[i] % 10

            result[i + 1] += add
            result[i] = left

        return "".join([str(i) for i in result[::-1] ]).lstrip("0")


if __name__ == '__main__':
    r = Solution().multiply("123", "456")
    print(r)
