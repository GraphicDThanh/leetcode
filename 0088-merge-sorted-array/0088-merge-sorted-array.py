class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # last element is total length (m + n) - 1
        last = m + n - 1
        
        # two pointers will be on m and n
        # until one of them out of elements
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                # if value at m smaller than value at n
                # set last value on nums1 to become value at m
                nums1[last] = nums1[m - 1]
                
                # reduce m to check next item (from right to left)
                m -= 1
            else:
                # if value at m larger than value at n
                # set last value on nums1 to become value at n
                nums1[last] = nums2[n - 1]
                
                # reduce n to check next item (from right to left)
                n -= 1
            
            # reduce the last element
            last -= 1

        # the rest of nums2 if still exists
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
 
        