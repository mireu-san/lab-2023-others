# hash table
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {} 
        answer = []
        odd = 0

        for word in s:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        for times in count.values():
            answer.append(times)
            if times % 2 != 0:
                odd += 1
        if odd != 0:
            return sum(answer) - odd + 1
        elif odd == 0:
            return sum(answer) - odd
        