class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize two pointers, slow and fast
        slow, fast = 0, 1  # slow points to the first element, and fast points to the next element

        # loop while fast pointer is within the array boundary
        while fast in range(len(nums)):
            # if the current slow and fast pointers point to the same value,
            # it means we've found a duplicate
            if nums[slow] == nums[fast]:
                # so, increment the fast pointer to find the next unique element
                fast += 1
            else:
                # if the slow and fast pointers point to different values,
                # it means we've found a unique element
                # so, move this unique element to the position next to where the slow pointer is pointing
                nums[slow+1] = nums[fast]
                # and then, we increment both pointers
                fast += 1
                slow += 1

        # in the end, slow pointer will be at the last unique element,
        # and since slow is 0-indexed, we return slow + 1, which is the count of unique elements
        return slow + 1
