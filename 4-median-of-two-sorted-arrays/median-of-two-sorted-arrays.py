class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        md = nums1 + nums2
        md.sort()
        gg = len(md)

        if gg%2 == 1:
            return md[gg//2]
        else:
            return (md[int(gg/2)] + md[int(gg/2) - 1])/2