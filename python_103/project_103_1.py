class Bike():
    sold = 'not sold'
    def __init__(self, description, cost, sale_price, condition):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
    
    def get_description(self):
        print(self.description)
    
    def get_cost(self):
        print(f'bike cost is ${self.cost}')
    
    def get_sale_price(self):
        print(f'current sale price is ${self.sale_price}')
    
    def get_condition(self):
        print(f'bike condition is {self.condition}')
    
    def get_sold(self):
        print(f'bike is {self.sold}')

    def update_sale_price(self, sale_price):
        if self.sold == 'sold':
            print('Action not allowed, Bike has already been sold')
        elif self.sale_price > sale_price:
            print(f'bid amount is less than current sale price which is ${self.sale_price}')
        else:
            self.sale_price = sale_price
            print(f'sale price successfully updated')
            self.get_sale_price()
    
    def sell(self):
        self.sold = 'sold'
        print(f'bike successfully sold for ${self.sale_price}')

################
def main():
    bike1 = Bike(description= 'Univega Alpina, orange', cost= 200, sale_price= 600, condition= 'Good')
    bike1.get_description()
    bike1.get_condition()
    bike1.get_sold()
    bike1.get_cost()
    bike1.get_sale_price()
    bike1.update_sale_price(1000)
    bike1.update_sale_price(900)
    bike1.sell()
    bike1.update_sale_price(1100)


if __name__ == '__main__':
    main()