class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
         nums = [3,4,5,1,2]

        minimum is where larger followed by smaller value e.g. 5 followed by 1
        

        [4,5,6,7,0,1,2]
         l
               m
                     r     

        binary search on nums:
            if nums[r] > nums[mid]:
                check left 
            else
                check right (mid +1)
        """
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[r]