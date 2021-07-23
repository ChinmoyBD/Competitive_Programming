class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        mergedList = []
        len1, len2 = len(nums1), len(nums2)
        index1 = index2 = 0

        while index1 < len1 and index2 < len2:
            if nums1[index1] < nums2[index2]:
                mergedList.append(nums1[index1])
                index1 += 1
            else:
                mergedList.append(nums2[index2])
                index2 += 1

        if index1 < len1:
            mergedList.extend(nums1[index1:])
        elif index2 < len2:
            mergedList.extend(nums2[index2:])
        nm = len1+len2
        if nm % 2 == 0:
            return float((mergedList[nm//2] + mergedList[(nm//2) - 1]) / 2)
        else:
            return float(mergedList[nm//2])


ob = Solution()
print(ob.findMedianSortedArrays([2], []))