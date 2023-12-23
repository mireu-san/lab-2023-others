def solution(n):
    num_list = list(str(n))

    num_list.sort(reverse=True)

    return int("".join(num_list))


# 오히려 이렇게 리스트를 받아서, 정렬 후 int 로 변환해서 join 하는 게 확실함.


#     reversed_num = str((n)[::-1])
#     if n < 0:
#         reversed_num = "-" + reversed_num[:1]
#     return int(reversed_num)


# def solution(n):
#     for i in range(n):
#         i.int(reverse(n))
#     return n
