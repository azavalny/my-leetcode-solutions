class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        sorted nums
        remove selected duplicates in place st each element appears at most twice in same relative order

        first k elements of array w/ deduped elements, after dosent matter
        return k 

        O(1) memory

        [1,1,1,2,2,3]
             i
             remove index 2, shift all to right by 1
        [1, 1, 2, 2, 3, _]


        [0,0,1,1,1,1,2,3,3]
                   i
        l=0
        r=9

        O(n^2logn)
        until no triplets left:
            find triplet w/ bin search from index 0 to len(nums)-how many triplets you've removed so far
                dosen't matter which bc input is sorted, all triplets grouped together anyway
            replace it by shifting all elements right of it one space (i becomes i+1) and stop before last element
        return len(nums) - how many triplets you had to remove


Output: 7, nums = [0,0,1,1,2,3,3,_,_]    

            [0,0,1,1,1,1,2,3,3]
                     l
                         i
O(n)        
    for i in range:
        if last 3 elments not same:
            swap i, l
            increment l
    return l

    [0,0,1,1,1,1,2,3,3]
             l
               i
        """
        l=0
        for i in range(len(nums)):
            current = nums[i]
            before_left = nums[l-1] if l-1 >= 0 else None
            before_before_left = nums[l-2] if l-2 >= 0 else None
            if current == before_left == before_before_left:
                continue
            nums[i], nums[l] = nums[l], nums[i]
            l +=1
        return l