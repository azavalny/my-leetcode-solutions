class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        sum of all XOR totals for every subset 2^n

        [1, 3]
        
        [1] - 0 XOR 1 = 1
        [1, 3] - 0 XOR 1 XOR 3 = 2
        [3] - 0 XOR 3 = 3

                 [  ]
                /    |
               1     3
              / \       
             3  []     

    total_sum = 0
        backtrack(i, cur_sum):
            if i at end total_sum += cur_sum
                return
            new_sum = cur_sum XOR nums[i]
            backtrack(i+1, new_sum)
            backtrack(i+1, cur_sum)
        """
        sol = 0

        def backtrack(i, cur_sum):
            nonlocal sol
            if i == len(nums):
                sol += cur_sum
                return
            for i in range(i, len(nums)):
                backtrack(i + 1, cur_sum ^ nums[i])

            sol += cur_sum
        backtrack(0, 0)
        return sol