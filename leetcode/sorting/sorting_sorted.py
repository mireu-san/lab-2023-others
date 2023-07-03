class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        sorted_with_letter = sorted(set(letters + [target]))
        index_target = sorted_with_letter.index(target)
        if index_target == len(sorted_with_letter) - 1:
            return sorted_with_letter[0]
        return sorted_with_letter[index_target + 1]


# or

# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         for i in letters:
#             if target != i and sorted([target, i])[1] == i:
#                return i
#         return letters[0]
