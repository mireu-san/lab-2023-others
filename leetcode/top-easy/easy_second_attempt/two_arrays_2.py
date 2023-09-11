# hash example:
class Solution:
    def intersect(self, nums1, nums2):
        # approach: use a hash map to store counts of nums in nums1

        return list(filter(self.is_in(nums1), nums2))

    def is_in(self, nums):
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        def is_in_map(target):
            if hash_map.get(target, 0):
                hash_map[target] -= 1
                return True
            return False

        return is_in_map
    
# two pointers:
class Solution:
    def intersect(self, nums1, nums2):
        # approach: sort two lists and use two pointers to compare

        nums1.sort()
        nums2.sort()
        
        p1 = p2 = 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1]
            num2 = nums2[p2]

            if num1 < num2:
                p1 += 1
            elif num1 > num2:
                p2 += 1
            else:
                result.append(num1)
                p1 += 1
                p2 += 1

        return result