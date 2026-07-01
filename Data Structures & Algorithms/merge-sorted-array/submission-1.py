class Solution:
    def merge(
        self,
        nums1: List[int],
        m: int,
        nums2: List[int],
        n: int,
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2

        def myMerge(start, midpoint, end):
            tmp = []
            i = start
            j = midpoint

            while i < midpoint and j < end:
                if nums1[i] <= nums1[j]:
                    tmp.append(nums1[i])
                    i += 1
                else:
                    tmp.append(nums1[j])
                    j += 1
            
            if i == midpoint:
                tmp.extend(nums1[j:end])
            else:
                tmp.extend(nums1[i:midpoint])
            
            nums1[start:end] = tmp
        
        myMerge(0, m, m+n)
