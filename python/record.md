# 개인 메모:
시프트 연산(shift operation), in 연산자, is 연산자는 각각 다른 기능을 가지고 있습니다.

시프트 연산(shift operation)은 비트(bit) 단위로 이동(shift)하는 연산입니다. 파이썬에서는 비트 단위 시프트 연산자 <<와 >>를 제공합니다. 왼쪽 시프트 연산자 <<는 비트열을 왼쪽으로 이동시키는 연산이며, 오른쪽 시프트 연산자 >>는 비트열을 오른쪽으로 이동시키는 연산입니다.

예를 들어, a = 0b1100이라고 할 때, a << 2를 하면 0b110000이 되고, a >> 1을 하면 0b0110이 됩니다.

in 연산자는 시퀀스(sequence) 자료형 안에 어떤 값이 있는지를 검사하여 True나 False를 반환하는 연산자입니다. 시퀀스 자료형에는 리스트(list), 튜플(tuple), 문자열(string), 셋(set) 등이 있습니다. in 연산자는 해당 값이 시퀀스 자료형 안에 있으면 True를, 없으면 False를 반환합니다.

예를 들어, 다음과 같은 리스트가 있을 때, 2 in [1, 2, 3]은 True를 반환하고, 4 in [1, 2, 3]은 False를 반환합니다.

is 연산자는 두 개의 객체가 동일한 객체인지를 검사하는 연산자입니다. is 연산자는 객체의 식별 번호(identity)를 비교합니다. 즉, 두 객체의 메모리 주소가 같은지를 비교합니다. 따라서 is 연산자는 객체의 값이 같은지를 비교하는 것이 아니라, 객체 자체가 같은 객체인지를 비교합니다.

예를 들어, a = [1, 2, 3]이라고 할 때, b = a라고 하면 b is a는 True를 반환합니다. 이는 b가 a와 같은 리스트 객체를 참조하고 있기 때문입니다. 반면, b = [1, 2, 3]이라고 할 때, b is a는 False를 반환합니다. 이는 b와 a가 서로 다른 리스트 객체를 참조하고 있기 때문입니다.