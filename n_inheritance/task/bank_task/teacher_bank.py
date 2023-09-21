def check(*, key, value):                               # 클로져 함수에 key 값과 value 값을 전달 받는다
    def set_target():
        for bank in Bank.banks:                         # Bank 클래스의 banks리스트([[],[],[]]의 bank에서
            for user in bank:                           # 각 bank의 user 에서
                if user.__getitem__(key) == value:      # user의 밸류 값과 입력받은 밸류 값이 같으면
                    return user                         # user를 리턴하고
        return None                                     # 같지 않으면 None을 리턴한다.

    return set_target                                   # 그 값이 set_target에 담기고 check에 리턴


class Bank:                                             # Bank 클래스 선언
    total_count = 3
    banks = [[] for i in range(total_count)]            # 은행의 수 만큼 리스트안에 리스트를 만드는 부분

    # self로 주소값을 받아오고 생성자를 선언하는 부분
    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):

        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money
        self.object = self                              # 객체의 주소값에 접근하기위해 , dic 때문에

    @classmethod  # init에서 선언된 생성자를 변경할 때 사용한다.
    def open_account(cls, owner: str, account_number: str, phone: str, password: str, money: int, bank_choice: int):


        bank = [
            ShinHan(owner, account_number, phone, password, money),
            KookMin(owner, account_number, phone, password, money),
            KaKao(owner, account_number, phone, password, money)
        ][bank_choice - 1]          # 입력받은 은행의 클래스를 -1하여 인덱스로 접근
        cls.banks[bank_choice - 1].append(bank.__dict__)                    # 선택한 은행의 인덱스에 딕셔너리로 추가
        return bank

    @staticmethod           # 해당로직은 은행 클래스에서 전부 사용되기 때문에 전체 객체에 반영하기 위해 staticmethod로 선언
    def check_account_number(account_number: str) -> dict:
        return check(key='account_number', value=account_number)() # 입력받은 account_number와 딕셔너리의 account_number의
                                                                   # 값을 check함수로 비교

    @staticmethod
    def check_phone(phone: str) -> dict:                            # 입력받은 phone과 딕셔너리의 phone의
        return check(key='phone', value=phone)()                    # 값을 check함수로 비교

    def deposit(self, money: int):                                  # 입금함수 선언
        self.money += money                                         # 입금 금액을 더하여 self.money 담아준다

    def withdraw(self, money: int):                                 # 출금함수 선언
        self.money -= money                                         # 출금 금액을 빼서 self.money 담아준다

    def show_balance(self) -> int:                                  # 남은 잔액 보여주는 함수
        return self.money

    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


class ShinHan(Bank):                                            # 신한은행(자식 클래스) 클래스 선언, Bank는 부모 클래스
    def deposit(self, money: int):                              # 수수료를 제외 한 입력 받은 입금 금액의 50% 가 money에 담기고
        money /= 2
        super().deposit(money)                                  # 부모 클래스인 Bank의 deposit 함수의 매개변수가 된다.


class KookMin(Bank):                                            # 국민은행(자식 클래스) 클래스 선언, Bank는 부모 클래스
    def withdraw(self, money: int):                             # 입력 받은 출금에 수수료 50%를 더해 money에 담는다
        money *= 1.5
        super().withdraw(int(money))                            # 부모 클래스인 Bank의 withdraw 함수의 매개변수가 된다.


class KaKao(Bank):                                              # 카카오 뱅크(자식 클래스) 클래스 선언, Bank는 부모 클래스
    def show_balance(self) -> int:                              # 조회시 반액이 되어야 하기 때문에 2로 나누어 self.money에 담는다
        self.money /= 2
        return super().show_balance()                           # 부모 클래스인 Bank의 show_balance함수에 리턴


if __name__ == '__main__':

    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    bank_names = [ShinHan, KookMin, KaKao]
    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:                                                     # while 반복문에서 4를 입력 받으면 탈출
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break

        while True:
            menu_choice = int(input(menu))                          # while 반복문에서 4를 입력 받으면 탈출
            if menu_choice == 5:
                break

            # 개설
            if menu_choice == 1:                                    # 1을 입력받으면
                owner = input(owner_message)                        # owner 입력

                while True:
                    account_number = input(account_number_message)              # 계좌번호를 입력받아
                    if Bank.check_account_number(account_number) is None:       # Bank 클래스의 check_account_number 함수를
                        break                                                   # 실행하여 리턴값이 None 이면 탈출

                while True:
                    phone = input(phone_message)                                # 폰넘버를 입력받아
                    if Bank.check_phone(phone) is None:                         # Bank 클래스의 check_phone함수르 실행하여
                        break                                                   # 리턴값이 None 이면 탈출

                while True:
                    password = input(password_message)                          # 패스워드가 4자리가 아니면 반복 물어보고
                    if password.__len__() == 4:                                 # 4자리여야 탈출
                        break

                money = int(input(money_message))

                user = None

                # 아래의 분기별 은행 분석을 한 줄로 변경!
                user = Bank.open_account(owner, account_number, phone, password, money, bank_choice)

                # # 신한 은행
                # if bank_choice == 1:
                #     user = ShinHan.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # # 카카오 뱅크
                # elif bank_choice == 2:
                #     user = KaKao.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # # 국민 은행
                # elif bank_choice == 3:
                #     user = KookMin.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # print(user, Bank.banks, sep="\n")

            # 입금
            elif menu_choice == 2:                                          # 2를 입력 받으면
                # 입금은 개설한 은행에서만 가능
                account_number = input(account_number_message)              # 계좌번호를 입력받고
                user = Bank.check_account_number(account_number)            # Bank 클래스의 check_account_number 함수를

                if user is not None:                                        # 실행하여 리턴값이 None이 아니면
                    if type(user["object"]) == bank_names[bank_choice - 1]: # bank_choice에 -1하여 bank_names의 인덱스 값과 
                                                                            # user["object"]의 type이 같으면
                        if user.__getitem__("password") == input(password_message): # 패스워드를 입력받고 user의 패스워드의
                                                                                    # 밸류값과 같으면
                            deposit_money = int(input(deposit_message))         # 입금 금액을 입력받아 deposit_money에 담는다
                            # 객체를 가져와서 deposite()실행
                            user.__getitem__("object").deposit(deposit_money)
                else:                                                           # 그렇지 않으면 에러메시지 출력
                    print(error_message)
            # 출금
            elif menu_choice == 3:                                          # 3을 입력받아
                account_number = input(account_number_message)              # 계좌번호를 입력받고
                user = Bank.check_account_number(account_number)            # Bank 클래스의 check_account_number 함수를
                if user is not None:                                        # 실행하여 리턴값이 None이 아니면
                    if user.__getitem__("password") == input(password_message):     # 패스워드를 입력받고 user의 패스워드의
                                                                                    # 밸류값과 같으면
                        withdraw_money = int(input(withdraw_message))       # 출금액을 입력받아 withdraw_money에 담는다
                        if user.__getitem__("object").money >= withdraw_money: # 객체의 돈이 출금액 이상이면
                            user.__getitem__("object").withdraw(withdraw_money) # 객체를 가져와서 withdraw()실행 
                        else:                                               # 그렇지 않으면
                            print("대출을 진행할까요?")                        # 대출 메시지 실행
                else:                                               
                    print(error_message)
            # 잔액
            elif menu_choice == 4:                                            # 4를 입력받아
                account_number = input(account_number_message)                # 계좌번호를 입력받고
                user = Bank.check_account_number(account_number)              # Bank 클래스의 check_account_number 함수를
                if user is not None:                                          # 리턴값이 None이 아니면
                    if user.__getitem__("password") == input(password_message):        # 패스워드를 입력받고 user의 패스워드의
                                                                                       # 밸류값과 같으면
                        print(f'현재 잔액: {user.__getitem__("object").show_balance()}') # 객체를 가져와서 show_balance()실행

                else:                                                         # 그렇지 않으면
                    print(error_message)                                      # 에러메시지 출력