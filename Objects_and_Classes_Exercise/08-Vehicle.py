# 08. Vehicle
class Vehicle:
    owner = None

    def __init__(self, vehicle_type: str, model: str, price: int):
        self.type = vehicle_type
        self.model = model
        self.price = price

    def buy(self, money: int, buyer: str):
        if self.price > money:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return 'Car already sold'
        else:
            self.owner = buyer
            change = money - self.price

            return f'Successfully bought a {self.type}. Change: {change:.2f}'

    def sell(self):
        if self.owner is None:
            return 'Vehicle has no owner'

        self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'
