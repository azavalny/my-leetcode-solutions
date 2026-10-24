class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        perfect square = number that is square of an integer
            no sqrt()


        binary search from 1 to num
            if mid^2 equals num
            elif too big search left half
            else search right half
        """
        l = 0
        r = num

        while l <= r:
            mid = (l + r)//2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                r = mid -1
            else:
                l = mid + 1
        return False