# 사용자가 구매하는 물건의 가격이 10000원 이상이면
# 5% 할인을 해준다.
# 재고에서 사용자가 구매한 물품 갯수 만큼 차감된다.


class Market:
    # 상품명, 상품가격, 상품 재고
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self,customer):
        total_price = self.price * customer.number
        final_price = 0

        if total_price  > 10000 :
            final_price = total_price * 0.95

        else :
            final_price = total_price

        customer.money -= int(final_price)
        self.stock -= customer.number




class Customer:
    # 이름, 갯수

    def __init__(self, name, number, money):
        self.name = name
        self.number = number
        self.money = money



market = Market("커피", 2000, 50)
customer1 = Customer("이서호", 10, 20000)
customer2 = Customer("홍길동", 2, 10000)

market.sell(customer1)
market.sell(customer2)


print(customer1.money)
print(customer2.money)
print(f"남은 재고는 {market.stock}개 입니다.")
