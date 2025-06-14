class PaymentBase:
    def __init__(self, amount: int):
        self.amount: int = amount

    def process_payment(self):
        pass

class CreditCard(PaymentBase):
    def process_payment(self):
        msg = f"Credit card payment: {self.amount}"
        print(msg)

class PayPal(PaymentBase):
    def process_payment(self):
        msg = f"Paypal payment: {self.amount}"
        print(msg)


if __name__ == "__main__":
    payments = [CreditCard(100), PayPal(200)]
    for payment in payments:
        payment.process_payment()