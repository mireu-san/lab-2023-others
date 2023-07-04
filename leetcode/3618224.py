class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters_length = len(letters)
        low = 0
        high = letters_length - 1

        if target < letters[low] or target >= letters[high]:
            return letters[low]

        while low <= high:
            middle = (low + high) // 2
            cancidate = letters[middle]

            if target < cancidate:
                high = middle - 1

            if target >= cancidate:
                low = middle + 1

        return letters[low]
