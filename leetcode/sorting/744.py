# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# non decreasing order. at least two differnet characters.

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
# https://docs.python.org/3/library/bisect.html


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        type letters: List[str]
        type target: str
        rtype: str
        """

        # if the number if out of bound
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        low = 0
        high = len(letters) - 1
        while low <= high:
            mid = (high + low) // 2

            if (
                target >= letters[mid]
            ):  # in binary search, this would be only greater than.
                low = mid + 1

            if target < letters[mid]:
                high = mid - 1

        return letters[low]
