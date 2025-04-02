class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        # Append remaining elements
        res += nums1[i:]
        res += nums2[j:]

        totalLen = (len(nums1)+len(nums2))
        mid = totalLen // 2
        
        if totalLen % 2 == 1:
            return res[mid]
        else:
            return (res[mid - 1] + res[mid]) / 2