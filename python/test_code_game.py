import random


class PlayerFactory:
    def __init__(self, name, health, strength, agility, intelligence):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def __str__(self):
        return f"{self.name}, 체력: {self.health}, 힘: {self.strength}, 민첩: {self.agility}, 지능: {self.intelligence}"


# 주인공 이름 생성기 함수
def name_designator():
    pre_name = ["알렉스", "메이슨", "예소드", "바바라", "벤티", "헤세드", "나인하트"]
    name = "".join(random.choices(pre_name, k=1))
    return name.capitalize()


# 주인공 생성
주인공 = PlayerFactory(name_designator(), 10000)
print(주인공)
