# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums 리스트의 길이가 1 이하라면, 그 길이를 그대로 반환
        if len(nums) <= 1:
            return len(nums)
        
        # nums 리스트의 길이가 2 이상이라면, nums 리스트의 첫번째 요소를 기준으로 잡고,
        # nums 리스트의 두번째 요소부터 마지막 요소까지 반복문을 돌면서,
        # nums 리스트의 첫번째 요소와 같은 요소가 있다면, 그 요소를 제거한다.
        # 그리고 nums 리스트의 길이를 반환한다.
        # 요약: 2개 포인터 초기화 및 write & read 모두 0에서 시작.
        write = 0
        read = 1

        # read 포인터가 nums 리스트의 끝에 도달할 때까지 반복
        while read < len(nums):
            # if read pointer element + write pointer element 가 다르면, 
            if nums[read] != nums[write]:
                # write pointer 를 1 증가시키고, (한칸 앞으로 이동)
                write += 1
                # write pointer 가 가리키는 곳에 read pointer 가 가리키는 요소를 복사한다.
                nums[write] = nums[read]
            # read pointer 를 1 증가시킨다. (한칸 앞으로 이동)
            read += 1

        # nums 리스트의 길이를 반환한다. (write 포인터 위치, 0에서 시작했으니 1을 더함)
        return write + 1
