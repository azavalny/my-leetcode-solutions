class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        """
        time[i] = time taken by ith bus to complete one trip
        same bus can do multiple trips and all of the buses can do concurrent trips

        find min time for all buses to complete at least total trips
        
        time = [1,2,3], totalTrips = 5

        1, 0, 0
        2, 1, 0
        3, 1, 1 max reached totalTrips

        brute force loop for every time until max(trips) reaches totalTrips in O(n^2)

        time = [2] totalTrips =4

        time = [1,2,3], totalTrips = 5

bin search over time range
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
l
            m
                                  r
    is_valid(mid)
        for each bus:
            accumulate time[i]//mid
        is total more than totalTrips?

        O(nlogn)
        binary search over times from t = 1 to min(time)*totalTrips to find min
            check if totalTrips can be completed by all buses in under mid time
            if true, compare min and check left half
            else check right half
        """
        def is_valid(mid):
            trips = 0
            for t in time:
                trips += mid//t
            return trips >= totalTrips
        l = 1
        r = min(time)*totalTrips
        sol = r

        while l <= r:
            mid = (l + r)//2
            if is_valid(mid):
                sol = min(sol, mid)
                r = mid -1
            else:
                l = mid + 1
        return sol