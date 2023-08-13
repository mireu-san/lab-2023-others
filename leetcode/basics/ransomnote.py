class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Note: Counter is a subclass of dict. 
        # It is an unordered collection where elements are stored as dictionary keys 
        # and their counts are stored as dictionary values.
        note, mag = Counter(ransomNote), Counter(magazine)
        
        # if note is a subset of mag, then return True!
        if note & mag == note: 
            return True
        return False