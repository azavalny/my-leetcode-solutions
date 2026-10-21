class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        dosent steal from adjacent homes
        capability = max house along plan

        return minimum (max house along plan of at least k houses)

        nums = [2,3,5,9], k = 2
        - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
        - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
        - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
        min is 5

        brute force O(n^2) search to find maxes of each plan then min of capabilities of each plan
        binary search O(nlogn) over capabilities(from smallest to largest possible house):
            can I can rob at least k houses never robbing a house more than mid?
                compare with current min
                check left half
            else check right half
        """
        def is_valid(max_capability):
            valid_houses = 0
            robbed_previous = False
            for i, h in enumerate(nums):
                if h <= max_capability and not robbed_previous:
                    valid_houses +=1
                    robbed_previous = True
                else:
                    robbed_previous = False
            if valid_houses >= k:
                return True
            return False
        l = min(nums)
        r = max(nums)
        sol = r

        while l <= r:
            mid = (l + r)//2
            if is_valid(mid):
                sol = min(sol, mid)
                r = mid -1
            else:
                l = mid +1
        return sol