def 삽입정렬(데이터):
    최종결과값 = []
    while 데이터:
        꺼낸값 = 데이터.pop(0)
        들어갈위치 = len(list(filter(lambda x: x < 꺼낸값, 최종결과값)))
        최종결과값.insert(들어갈위치, 꺼낸값)
    return 최종결과값


삽입정렬([199, 22, 33, 12, 32, 64, 72, 222, 233])
