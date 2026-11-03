class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        
        k rows
        ith row has i coins but last row may be incomplete
        return # of complete rows

        n is  large 2^31 ==> indicates binary search
            monotonicity in mid comparison because # of rows left

        brute force linear: loop to sum i from i=1 until sum > n
        n=5
        1*1+
        2*2+
        3*3 = 6 total possible coins so 6-5 = 1 missing coin

        binary search logn: search for max number of rows that fit n coins from 1 to n
            check if n coins can fit in mid rows:
                if too big search right half
                else search left half
        """
        l = 1
        r = n
        max_rows = 0
        while l <= r:
            mid = (l + r)//2
            # gaussian sum 1 to k is k(k+1)/2
            total_coins_mid = mid*(mid+1)//2
            if n >= total_coins_mid:
                max_rows = mid
                l = mid + 1
            else:
                r = mid -1
        return max_rows