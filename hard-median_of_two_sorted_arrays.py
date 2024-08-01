# beats 83.14% of solutions

# My first hard!

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # steps (not in order): check even/odd, increment from first in one list and
        # compare the numbers in the lists
        
        index1 = 0
        index2 = 0
        size1 = len(nums1)
        size2 = len(nums2)
        mid = (size1 + size2 + 1) // 2
        if size1 == 0:
            if size2 % 2 != 0:
                return nums2[size2 // 2]
            return float(nums2[int(round(size2 / 2))] + nums2[int(round(size2 / 2)) - 1]) / 2
        if size2 == 0:
            if size1 % 2 != 0:
                return nums1[size1 // 2]
            return float(nums1[int(round(size1 / 2))] + nums1[int(round(size1 / 2)) - 1]) / 2

        for i in range(mid):
            if index1 >= size1:
                store = nums2[index2]
                index2 += 1
            elif index2 >= size2:
                store = nums1[index1]
                index1 += 1
            elif nums1[index1] < nums2[index2]:
                store = nums1[index1]
                index1 += 1
            else:
                store = nums2[index2]
                index2 += 1
        
        if (size1 + size2) % 2 != 0:
            return store

        if index1 >= size1:
                store2 = nums2[index2]
        elif index2 >= size2:
            store2 = nums1[index1]
        else:
            store2 = min(nums1[index1], nums2[index2])
        return float(store + store2) / 2
