class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        peak = greater than neighbors

        an element is always considered to be strictly greater than a neighbor that is outside the array

        find index of any peak element in O(logn) -- otherwise sliding window would work

        nums[i] != nums[i + 1] for all valid i

        [1,2,3,1]
        [0 1 2 3]
         l
           m
               r
        [1,2,1,3,5,6,4]
         l
               m
                     r
        
        [1, 2, 3]
               l
               m
               r

        is_peak(index) = check if greater than values next to it including first and last element
        if middle greater than next two return
        else choose half with greater nums[i+1] or nums[i-1] value
            The values keep rising going right or left until we reach the ends so we'll likely find a peak if we go for the larger value

        
        """
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r)//2
            if mid < len(nums)-1 and nums[mid] < nums[mid+1]: #right greater
                l = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                return mid