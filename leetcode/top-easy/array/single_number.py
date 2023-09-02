class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 빈 hashset을 초기화합니다. 이 set은 짝을 이루지 않는 숫자를 추적합니다.
        hashset = set()
        
        # 주어진 리스트의 모든 숫자에 대해 반복합니다.
        for i in range(0, len(nums)):
            # 만약 현재 숫자가 이미 hashset에 있다면, 이 숫자는 짝을 이룹니다.
            # 따라서 hashset에서 제거합니다.
            if nums[i] in hashset:
                hashset.remove(nums[i])
            # 만약 현재 숫자가 hashset에 없다면, 이 숫자는 지금까지 한 번만 나타났습니다.
            # 따라서 hashset에 추가합니다.
            else:
                hashset.add(nums[i])
        
        # 모든 숫자를 처리한 후, hashset에 남아있는 숫자가 한 번만 나타나는 숫자입니다.
        # 이 숫자를 반환합니다.
        for j in hashset:
            return j