class Solution:
    """
    pickIndex = picks index and returns 
        p(i) = w[i]/sum(w)

    10^4 * 10^5 = 10^9 + sorting weights for higher probabilities indicates binary search


    Solution([1, 3])
element      1    3
cumSum       1    4
range      (0,1]  (1,4]
from cumSum


    random_num = sum(w)*random()
    bin search on prefix sum to find smallest sum not exceeding random_num from 0 to end of prefix sum array
    """

    def __init__(self, w: list[int]):
        self.prefix = [0]
        for w_i in w:
            self.prefix.append(self.prefix[-1] + w_i)
        

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        l, r = 1, len(self.prefix)
        while l < r:
            mid = (l + r)//2
            if self.prefix[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()