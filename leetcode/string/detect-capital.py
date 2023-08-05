class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Count the number of uppercase characters in the word
        upper_case_count = sum(1 for c in word if c.isupper())

        # All characters are uppercase
        all_upper = upper_case_count == len(word)

        # All characters are lowercase
        all_lower = upper_case_count == 0

        # Only the first character is uppercase
        only_first_upper = upper_case_count == 1 and word[0].isupper()

        # Return whether any of the valid patterns is true
        return all_upper or all_lower or only_first_upper
