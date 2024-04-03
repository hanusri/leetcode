from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # default dict hashmap
        map = defaultdict(list)
        count = 0
        # enumerate each number into index and value
        for i, num in enumerate(nums):

            # we check if the number is a key to our dictionary
            if num in map:

                # if it is, loop through each index that is associated
                # to that number and check if the product of the current
                # index and the index associated to the number is divisible
                # by k
                for index in map[num]:
                    if index * i % k == 0:
                        # if it is divisible, increment count
                        count += 1

            # after checking the hashmap, append the index to the key of the
            # current number
            map[num].append(i)
        
        # return the total count
        return count