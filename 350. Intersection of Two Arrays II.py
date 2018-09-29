from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        counter1 = Counter()
        counter2 = Counter()

        counter1.update(nums1)
        counter2.update(nums2)

        ans = []
        for key in counter1.keys():
            if key in counter2:
                for i in range(min(counter1[key], counter2[key])):
                    ans.append(key)

        return ans
