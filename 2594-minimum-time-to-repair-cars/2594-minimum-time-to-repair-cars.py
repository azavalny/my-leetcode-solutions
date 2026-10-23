class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """
        rank r repair n cars in r*n^2 min
        cars waiting
        return min time to repair all cars
            All the mechanics can repair the cars simultaneously

         ranks = [4,2,3,1], cars = 10

        4*2^2 = 16
        2*2^2 = 8
        3*2^2 = 12
        1*4^2 = 16

        ranks = [5,1,8], cars = 6

        5*1^2 = 5 min
        1*4^2 = 16
        8*1^2 = 8
        
        O(max(ranks)log(n^2) = 2*max(ranks)log(n))
        bin search to find min(max time to repair any group of cars) from min(ranks)*1^2 to min(ranks)*cars^2
            given mid budget whats the most any single mechanic could do on their own?
                if so compare min and check left half
            else check right half

        is_valid(mid time):
            given mid budget, r*n^2 <= mid
                                n <= sqrt(mid/r)
                                sum these up and check if greater than or equal to cars
        """
        def is_valid(mid):
            total_cars = 0
            for r in ranks:
                total_cars += int((mid/r)**0.5)
            return total_cars >= cars
        l = 1
        r = min(ranks)*(cars**2)
        sol = r

        while l <= r:
            mid = (l + r)//2
            if is_valid(mid):
                sol = min(sol, mid)
                r = mid -1
            else:
                l = mid + 1
        return sol