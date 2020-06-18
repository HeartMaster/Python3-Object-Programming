class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError('Only integers can be added')
        if integer%2:
            raise ValueError('Only even numbers can be added')
        super().append(integer)


class InvalidWithdrawal(Exception):
    def __init__(self,balance,amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance =balance

    def overage(self):
        return self.amount - self.balance

# raise InvalidWithdrawal(25,50)


