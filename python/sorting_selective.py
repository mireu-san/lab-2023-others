def 선택정렬(데이터):
    최종결과값 = []
    while 데이터:
        최솟값 = min(데이터)
        최종결과값.append(최솟값)
        데이터.remove(최솟값)
    return 최종결과값


선택정렬([199, 22, 33, 12, 32, 64, 72, 222, 233])
