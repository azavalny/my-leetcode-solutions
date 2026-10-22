class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        """
        n stores
        quantities product amounts

        distribute all products st:
            a store can only be given at most one product type but any amount
        minimize the max number of products given to any store

        n = 6, quantities = [11,6]

11 = 2, 3, 3, 3
6 = 3, 3

        n = 7, quantities = [15,10,10]

15 = 5 5 5
10 = 5 5
10 = 5 5
        q = [11], n=6
        2, 2, 2, 2, 2, 1

    1 2 3 4 5 6
    l
        m
              r

        binary search to find min product/store over 1 to max(quantities):
            with cap of mid per store, do all product types together need at most n stores?
            sum ceil(store[i]/mid) and see if you can use no more than n
                if so, compare min
                check left half
            else check right half
        """
        def is_valid(per_store_cap):
            stores_needed = 0
            for q in quantities:
                stores_needed += math.ceil(q/ per_store_cap)
            return stores_needed <= n
        l = 1
        r = max(quantities)
        sol = r

        while l <= r:
            mid = (l + r)//2

            if is_valid(mid):
                sol = min(sol, mid)
                r = mid -1
            else:
                l = mid + 1
        return sol