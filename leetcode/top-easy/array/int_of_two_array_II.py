from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []  # 결과를 저장할 빈 리스트 생성

        count = dict(Counter(nums1))  # nums1의 각 원소와 그 빈도수를 저장한 딕셔너리 생성

        # nums2의 각 원소에 대해
        for num in nums2:
            # 만약 해당 원소가 nums1에도 있고, 빈도수가 0이 아니라면
            if num in count and count[num] != 0:
                result.append(num)  # 결과 리스트에 추가
                count[num] = count[num] - 1  # 빈도수를 1 줄임

        return result  # 결과 반환
