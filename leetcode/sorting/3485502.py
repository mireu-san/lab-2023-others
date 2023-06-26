from sortedcontainers import SortedSet


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = SortedSet(nums)
        mx, cur = 0, 0
        for num in nums:
            if num - 1 in nums:
                cur += 1
            else:
                mx = max(mx, cur)
                cur = 1
        mx = max(mx, cur)
        return mx
