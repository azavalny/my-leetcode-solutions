class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        strengths of spells and potions

        valid pair is spell_i * potion_j >= success 

        return array of for each spell number of potions that form valid pair

        brute force O(nm)
        for each spell:
            check each potion if it forms successful pair

        Binary search on potions O(n *log(m))
        sort potions asc
            valid potions are only ever a suffix: A bigger potion only makes spell * potion bigger, so the valid ones form a suffix of the array
        for each spell:
            binary search on sorted potions to find smallest potion_j then set spells[i] to be len(potions)-j
                middle: check spell_i*potion_j >= success
                search left half as long as we got valid mid to find smaller, otherwise right half to find valid again
            if m was never found we set spells[i] to be null

        potions = [1,2,3,4,5], success = 7
                     l
                     m
                     r
spells = [5,1,3]
          i

potions = [1] success = 1
           l
           r
           m
spells = [1]
          i
potions = [1] success = 2
           l
           r
           m
spells = [1]
          i
        """
        output = [0]* len(spells)
        potions.sort()
        for i in range(len(spells)):
            l= 0
            r = len(potions)-1
            min_index = float("inf")
            while l <= r:
                mid = (l + r)//2
                if spells[i]*potions[mid] >= success:
                    min_index = min(min_index, mid)
                    r = mid -1
                else:
                    l = mid + 1
            
            if min_index < len(potions):
                output[i] = len(potions)-min_index
        return output