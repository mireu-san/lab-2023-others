def 계산(a, b, c):
    가격 = {"A등급": 1000, "B등급": 500, "C등급": 100}
    합계 = a * 가격["A등급"] + b * 가격["B등급"] + c * 가격["C등급"]
    return 합계


총합 = 계산(1, 2, 3)

if 총합 >= 10000:
    print("할인이 적용됩니다.")
    print(f"총 {총합 * 0.9} 가량의 노드를 내면 됩니다.")
else:
    print(f"총 {총합}노드를 내면 됩니다.")
