# 버스에 사람이 타면 좌석이 줄고
# 남은 잔액과 남은 좌석수 출력


class Bus:
    child_bus_fare = 1000
    adult_bus_fare = 1500



    def __init__(self, bus_number, bus_seat):
        self.bus_number = bus_number
        self.bus_seat = bus_seat


    def bus_in(self):

        left_seat = self.bus_seat - Customer.count_of_customer

        print(f'남은 좌석 수는 {left_seat}입니다.')


class Customer:
    count_of_customer = 0

    def __init__(self, age, money):
        Customer.count_of_customer += 1
        self.age = age
        self.money = money

    def get_change(self):
        change = 0
        if self.age > 19:
            change = self.money - Bus.adult_bus_fare

        else:
            change = self.money - Bus.child_bus_fare

        print(f"잔액은 {change}입니다.")


bus = Bus(9302,45)
customer1 = Customer(18, 10000)
customer2 = Customer(21, 10000)

customer1.get_change()
customer2.get_change()
bus.bus_in()