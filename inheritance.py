class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {recipient} successfully")
        else:
            print("Insufficient Amount to Send")


class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buy_airtime(self, amount):
        self.account_balance -= amount
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES airtime bought successfully")
        else:
            print("Insufficient Amount to buy Airtime")


class Business_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_number):
        super().__init__(account_balance, phone_number)
        self.business_number = business_number

    def receive_payment(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer")


personal = PersonalMpesa(2000, 79864765, 674536)
personal.send_money(300, 794853456)
personal.buy_airtime(150)

business = Business_Mpesa(5000, 783496751, 654321)
business.receive_payment(1000)
business.send_money(2000, 789412764, )