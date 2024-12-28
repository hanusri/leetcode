from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = dict()
        for item in nums1:
            map[item] = map.get(item, 0) + 1
        
        result = []
        for item in nums2:
            if map.get(item, 0) > 0:
                map[item] = map.get(item) - 1
                result.append(item)
        
        return result