class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        strings = [""] * (n + 1)

        num = 3
        while num <= n:
            strings[num] = "Fizz"
            num += 3

        num = 5
        while num <= n:
            strings[num] += "Buzz"
            num += 5

        for i in range(len(strings)):
            if not strings[i]:
                strings[i] = str(i)

        return strings[1:]