class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n  # If k is greater than n, we only need to move k % n steps.

        start = 0
        count = 0

        while count < n:
            current, prev = start, nums[start]

            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                # Break the loop if we return to the start position.
                if start == current:
                    break

            # Move to the next starting position.
            start += 1

        return nums
    
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/