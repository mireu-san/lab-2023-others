class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        if odd_count > 1:
            return len(s) - odd_count + 1
        return len(s)
    
# def longestPalindrome(self, s: str) -> int:
#     longest = ''
#     n = len(s)
#     for i in range(n):
#         for j in range(i+1,n+1):
#             word = s[i:j]
#             if word == word[::-1]:
#                 if len(word)>len(longest):
#                     longest = word          
#     return longest