class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums))[::-1]:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
        # l = 0
        # for r in range(len(nums)):
        #     if nums[r]:
        #         nums[l]=nums[r] = nums[r]
        #         l+=1
        # return nums