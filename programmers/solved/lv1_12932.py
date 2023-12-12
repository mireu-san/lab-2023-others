def solution(n):
    # 숫자를 string 으로 변환하고, 역순으로 정렬.
    reversed_str = str(n)[::-1]

    # 역순 된 string 을 숫자로 변환해서 list 에 추가.
    reversed_list = []
    # 그리고 반복문으로 하나씩 리스트 내부에 추가.
    for char in reversed_str:
        reversed_list.append(int(char))

    # 그렇게 해서, 요구사항대로 완성된 list 를 반환.
    return reversed_list
