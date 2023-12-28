def solution(absolutes, signs):
    result = 0

    # enumerate 와 유사하게, zip 을 사용하면 두 개의 리스트를 하나로 묶어준다.
    for num, sign in zip(absolutes, signs):
        # sign 이 True 이면 num 을 더하고, False 이면 num 을 뺀다.
        if sign == True:
            result += num

        else:
            result -= num

    return result


#  이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와
#  이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.

#  실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
