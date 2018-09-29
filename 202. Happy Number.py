def happy(n, seen):
    if n == 1 or n == 10 or n == 100:
        return True
    if n in seen:
        return False

    seen.add(n)
    count = 0
    for num in str(n):
        count += int(num) ** 2
    return happy(count, seen)


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return happy(n,set())