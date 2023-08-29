class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)) : 
            temp = dic.get(nums[i],2)
            if temp != 2 :
                return True
            dic[nums[i]] = 1
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # Initialize an empty set to keep track of seen numbers
#         seen = set()
        
#         # Loop through each number in the array
#         for num in nums:
#             # If the number is already in the set, it's a duplicate
#             if num in seen:
#                 return True
#             # Otherwise, add the number to the set
#             seen.add(num)
        
#         # If we reach this point, there are no duplicates
#         return False
    

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/