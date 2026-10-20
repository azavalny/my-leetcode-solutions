class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        """
        find max # candies/child given each child has same number of candies
            you cannot merge two piles together == cannot transfer candies from one pile to another
            so smallest pile of candies at the start bottlenecks entire giving process

        binary search from 1 to max(candies) to find max candies:
            middle valid if mid*k < sum(candies)
                check right half to find new max
            else check left half


        candies = [5,8,6], k = 3
19//3 = 6
    1 2 3 4 5
            l
            r
            m
max: 5

candies = [2,5], k = 11
sum(candies)//k == 0, return 0

        candies = [5,8,6], k = 5
1 2 3 4 5
      l
        m
        r
max: 5

[1,2,3,4,10], k= 5
        """
        if sum(candies)//k == 0:
            return 0
        l = 1
        r = sum(candies)//k
        sol = 0
        while l <= r:
            mid = (l + r)//2
            if sum(c // mid for c in candies) >= k: # how many sub piles of size mid you can cut
                sol = mid
                l = mid + 1
            else:
                r = mid -1
        return sol