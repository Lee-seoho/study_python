# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고
#
# 신한
#    입금 시 수수료 50%
# 국민
#    출금 시 수수료 50%
# 카카오
#    잔액조회 재산 반토막

class Bank:
    users = []

    def __init__(self, owner: str , account_number: str , phone: str , password: str , money: int ):
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    @classmethod
    def open_account(cls, owner: str, account_number: str, phone: str, password: str, money: int):
        cls.users.append(cls.__dict__)
        return cls(owner, account_number, phone, password, money)

    @staticmethod
    def check_account_number(account_number: str) -> bool:
        pass

    @staticmethod
    def check_phone(phone: str) -> bool:
        pass

    def deposit(self, money: int):
        money += money

    def withdraw(self, money: int):
        money -= money

    def show_balance(self) -> int:
        pass

class SinHan(Bank) :
    # 단위 %
    deposit_rate = 50

    def __init__(self, account_holder, account_num, phone_num, password, balance, deposit_money : int):
        super().__init__(account_holder, account_num,phone_num, password, balance)
        self.deposit_money = deposit_money

    def deposit_commission(self):
        return self.deposit_money * SinHan.deposit_rate * 0.01

    def account_balance(self):
        return self.balance + self.deposit_money - self.deposit_commission()



class Kookmin(Bank) :
    # 단위 %
    withdraw_rate = 50

    def __init__(self, account_holder, account_num, phone_num, password, balance, withdraw_money : int):
        super().__init__(account_holder, account_num,phone_num, password, balance)
        self.withdraw_money = withdraw_money

    def withdraw_commission(self):
        return self.withdraw_money * Kookmin.withdraw_rate * 0.01

    def account_balance(self):
        return self.balance - self.withdraw_commission() - self.withdraw_money


class KaKao(Bank):
    def __init__(self, account_holder, account_num, phone_num, password, balance ):
        super().__init__(account_holder, account_num,phone_num, password, balance)



info = {'account_holder': "이서호",
     'account_num': "12345678",
     'phone_num': "01011112222",
     'password': "4321",
     'balance': 10000}

info2 = {'account_holder': "홍길동",
     'account_num': "98765432",
     'phone_num': "01033334444",
     'password': "1234",
     'balance': 20000}


bank = Bank(wner, account_number, phone, password, money)

# print(bank.users)
#
# sinhan = SinHan("이서호", "12345678", "01011112222", "4321", 10000, 2000)
# print(sinhan.account_balance())
#
# kookmin = Kookmin("이서호", "12345678", "01011112222", "4321", 10000, 2000)
# print(kookmin.account_balance())