class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        result = []

        if nums1 == []:
            result = nums2

        if nums2 == []:
            result = nums1

        len1 = len(nums1)
        len2 = len(nums2)

        if len1 > len2:
            nums2, nums1 = nums1, nums2

        if len1 > 0 and len2 > 0:

            i = 0
            j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1
            if i < len(nums1):
                result.extend(nums1[i:])
            elif j < len(nums2):
                result.extend(nums2[j:])

        if result == []:
            return 0
        elif len(result) % 2 == 0:
            mid = len(result) / 2
            return (result[mid] + result[mid - 1]) / 2
        else:
            return result[len(result) // 2]






