# 이번달 대출 이자 구하기
# 금리 5%

class Bank:
    # 단위 %
    interest_rate = 5

    def __init__(self, name, locate):
        self.name = name
        self.locate = locate


class Customer:
    def __init__(self, name, loan_money):
        self.name = name
        self.loan_money = loan_money

    def cal_month_interest(self):
        month_interest = self.loan_money * Bank.interest_rate * 0.01 / 12
        print(f'{self.name}님이 {bank.name}은행에 내야할 이번 달 이자는 {int(month_interest)}만원 입니다.')


bank = Bank("기업은행", "잠실")



# 단위 : 만원
customer1 = Customer("이서호",10000)
customer2 = Customer("홍길동",20000)
customer1.cal_month_interest()
customer2.cal_month_interest()











