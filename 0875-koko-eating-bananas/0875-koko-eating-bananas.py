class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        return k (minimum eating speed of bananans/hr)
        each hour from 0 to h:
            eats k bananas from some pile[i] (all if less than k)

        [3, 6, 7, 11] h=8

        binary search from k=1 to k=max(piles) such that sum(math.ceil(pile[i]/k)) <= h

        for k=1 to max(piles):
            k = middle
            if hours <= h try smaller k otherwise do bigger k
        """
        def is_valid(mid):
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            return hours <= h
        l, r = 1, max(piles)
        mid = 1

        while l <= r:
            mid = l + (r-l)//2
            if is_valid(mid):
                r = mid -1
            else:
                l = mid + 1
        return l