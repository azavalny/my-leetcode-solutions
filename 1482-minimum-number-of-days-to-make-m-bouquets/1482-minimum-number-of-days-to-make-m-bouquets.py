class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        """
        to make bouquet, k adjacent flowers
        
        each flower used in only one bouquet (check if used)

        bloomDay_i = day the ith flower blooms
        
        find min # of days to wait to make m bouquets else -1
            monotonic because we can always wait more days but want to find min


        bloomDay = [1,10,3,10,2], m = 3, k = 1

After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
                l
                           r
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

[x, x, x, _, x], m=3,k=3
          l
             r


    is_valid:
        loop over each flower for r and if current flower is spawned check if (r-l)+1 == k:
            if so move l to r+1
            increment numBouquets

        if len(bloomDay) smaller than m*k return -1

        O(n log(max(bloomDay)))

        bin search from 1 to max(bloomDay) to find min # of days for is_valid:
            if current day is_valid(mid):
                compare w/ current min
                check left half
            else
                check right half because # of days too small

l 1 r 1000000000 mid 500000000
Bloomed search
Current flower blooms on day 0 with 500000000 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 500000000 as mid
Number of bloomed so far: 0 with num boquets 0
l 500000001 r 1000000000 mid 750000000
Bloomed search
Current flower blooms on day 0 with 750000000 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 750000000 as mid
Number of bloomed so far: 0 with num boquets 0
l 750000001 r 1000000000 mid 875000000
Bloomed search
Current flower blooms on day 0 with 875000000 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 875000000 as mid
Number of bloomed so far: 0 with num boquets 0
l 875000001 r 1000000000 mid 937500000
Bloomed search
Current flower blooms on day 0 with 937500000 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 937500000 as mid
Number of bloomed so far: 0 with num boquets 0
l 937500001 r 1000000000 mid 968750000
Bloomed search
Current flower blooms on day 0 with 968750000 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 968750000 as mid
Number of bloomed so far: 0 with num boquets 0
l 968750001 r 1000000000 mid 984375000
Bloomed search
Current flower blooms on day 0 with 984375000 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 984375000 as mid
Number of bloomed so far: 0 with num boquets 0
l 984375001 r 1000000000 mid 992187500
Bloomed search
Current flower blooms on day 0 with 992187500 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 992187500 as mid
Number of bloomed so far: 0 with num boquets 0
l 992187501 r 1000000000 mid 996093750
Bloomed search
Current flower blooms on day 0 with 996093750 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 996093750 as mid
Number of bloomed so far: 0 with num boquets 0
l 996093751 r 1000000000 mid 998046875
Bloomed search
Current flower blooms on day 0 with 998046875 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 998046875 as mid
Number of bloomed so far: 0 with num boquets 0
l 998046876 r 1000000000 mid 999023438
Bloomed search
Current flower blooms on day 0 with 999023438 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999023438 as mid
Number of bloomed so far: 0 with num boquets 0
l 999023439 r 1000000000 mid 999511719
Bloomed search
Current flower blooms on day 0 with 999511719 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999511719 as mid
Number of bloomed so far: 0 with num boquets 0
l 999511720 r 1000000000 mid 999755860
Bloomed search
Current flower blooms on day 0 with 999755860 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999755860 as mid
Number of bloomed so far: 0 with num boquets 0
l 999755861 r 1000000000 mid 999877930
Bloomed search
Current flower blooms on day 0 with 999877930 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999877930 as mid
Number of bloomed so far: 0 with num boquets 0
l 999877931 r 1000000000 mid 999938965
Bloomed search
Current flower blooms on day 0 with 999938965 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999938965 as mid
Number of bloomed so far: 0 with num boquets 0
l 999938966 r 1000000000 mid 999969483
Bloomed search
Current flower blooms on day 0 with 999969483 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999969483 as mid
Number of bloomed so far: 0 with num boquets 0
l 999969484 r 1000000000 mid 999984742
Bloomed search
Current flower blooms on day 0 with 999984742 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999984742 as mid
Number of bloomed so far: 0 with num boquets 0
l 999984743 r 1000000000 mid 999992371
Bloomed search
Current flower blooms on day 0 with 999992371 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999992371 as mid
Number of bloomed so far: 0 with num boquets 0
l 999992372 r 1000000000 mid 999996186
Bloomed search
Current flower blooms on day 0 with 999996186 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999996186 as mid
Number of bloomed so far: 0 with num boquets 0
l 999996187 r 1000000000 mid 999998093
Bloomed search
Current flower blooms on day 0 with 999998093 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999998093 as mid
Number of bloomed so far: 0 with num boquets 0
l 999998094 r 1000000000 mid 999999047
Bloomed search
Current flower blooms on day 0 with 999999047 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999047 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999048 r 1000000000 mid 999999524
Bloomed search
Current flower blooms on day 0 with 999999524 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999524 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999525 r 1000000000 mid 999999762
Bloomed search
Current flower blooms on day 0 with 999999762 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999762 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999763 r 1000000000 mid 999999881
Bloomed search
Current flower blooms on day 0 with 999999881 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999881 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999882 r 1000000000 mid 999999941
Bloomed search
Current flower blooms on day 0 with 999999941 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999941 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999942 r 1000000000 mid 999999971
Bloomed search
Current flower blooms on day 0 with 999999971 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999971 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999972 r 1000000000 mid 999999986
Bloomed search
Current flower blooms on day 0 with 999999986 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999986 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999987 r 1000000000 mid 999999993
Bloomed search
Current flower blooms on day 0 with 999999993 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999993 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999994 r 1000000000 mid 999999997
Bloomed search
Current flower blooms on day 0 with 999999997 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999997 as mid
Number of bloomed so far: 0 with num boquets 0
l 999999998 r 1000000000 mid 999999999
Bloomed search
Current flower blooms on day 0 with 999999999 as mid
Number of bloomed so far: 0 with num boquets 0
Current flower blooms on day 1 with 999999999 as mid
Number of bloomed so far: 0 with num boquets 0
l 1000000000 r 1000000000 mid 1000000000
Bloomed search
Current flower blooms on day 0 with 1000000000 as mid
Number of bloomed so far: 0 with num boquets 1
Current flower blooms on day 1 with 1000000000 as mid
Number of bloomed so far: 0 with num boquets 2
        """
        def is_valid_day(current_day):
            numBouquets = 0
            numBloomed = 0
            # print("Bloomed search")
            for f in range(len(bloomDay)):
                # print(f"Current flower blooms on day {f} with {current_day} as mid")
                if bloomDay[f] <= current_day:
                    numBloomed +=1
                else:
                    numBloomed = 0
                if numBloomed == k:
                    numBouquets+=1
                    numBloomed = 0
                # print(f"Number of bloomed so far: {numBloomed} with num boquets {numBouquets}")

            return numBouquets >= m

        if len(bloomDay) < m*k:
            return -1
        l = 1
        r = max(bloomDay)
        sol = float("inf")
        while l <= r:
            # print(f"l {l} r {r} mid {(l + r)//2}")
            mid = (l + r)//2
            if is_valid_day(mid):
                sol = min(sol, mid)
                r = mid -1
            else:
                l = mid + 1
        return sol
        if sol > max(bloomDay):
            return -1
        return sol