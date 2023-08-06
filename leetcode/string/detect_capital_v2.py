class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all the letters in the word are uppercase
        if word.isupper():
            return True
        
        # Check if all the letters in the word are lowercase
        elif word.islower():
            return True
        
        # Check if only the first letter in the word is uppercase and the rest are lowercase
        elif word[0].isupper() and word[1:].islower():
            return True
        
        # If none of the above conditions are met, the usage of capitals in the word is not right
        return False
