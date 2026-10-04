class Upi:
    def payment(self, amount):
        print("Payment through UPI")
        print("Amount:", amount)


class Creditcard:
    def payment(self, amount):
        print("Payment through Credit Card")
        print("Amount:", amount)


class Debitcard:
    def payment(self, amount):
        print("Payment through Debit Card")
        print("Amount:", amount)


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def start(self, amount):
        self.strategy.payment(amount)


amount = float(input("Enter payment amount: "))

choice = int(input("Choose payment mode (1=Upi, 2=Credit, 3=Debit): "))

match choice:
    case 1:
        Payment(Upi()).start(amount)
    case 2:
        Payment(Creditcard()).start(amount)
    case 3:
        Payment(Debitcard()).start(amount)
    case _:
        print("Invalid payment mode")