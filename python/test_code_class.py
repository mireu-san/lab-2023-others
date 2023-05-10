class UserInfo(object):
    def __init__(self, 고객명, 구매_횟수):
        self.name = 고객명
        self.purchase_count = 구매_횟수
        self.rating = self.criteria()

    def criteria(self):
        if self.purchase_count >= 40:
            return "Moon"
        elif self.purchase_count >= 30:
            return "VIP"
        elif self.purchase_count >= 20:
            return "Silver"
        elif self.purchase_count >= 10:
            return "Bronze"
        else:
            return "Happy Customer"

    def __str__(self):
        return f"고객명: {self.name}, 등급: {self.rating}"


customer_list = [
    UserInfo("알렉스", 111),
    UserInfo("메이슨", 254),
    UserInfo("매지션", 22),
    UserInfo("워리어", 8),
]

for customer in customer_list:
    print(customer)
