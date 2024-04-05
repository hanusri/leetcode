class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict = {}

        for num in nums2:
            while stack and stack[-1] < num:
                dict[stack.pop()] = num
            stack.append(num)

        return [dict.get(num, -1) for num in nums1]
        