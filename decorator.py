class Purchase:
    def calculate_cost(self):
        pass

# Қарапайым адамдар үшін сатылым
class RegularPurchase(Purchase):
    def __init__(self, cost):
        self.cost = cost

    def calculate_cost(self):
        return self.cost

# Бағалы клиенттер үшін абстрактный декоратор
class DiscountDecorator(Purchase):
    def __init__(self, decorated_purchase):
        self._decorated_purchase = decorated_purchase

    def calculate_cost(self):
        return self._decorated_purchase.calculate_cost()

# VIP клиенттер үшін деконатор
class VIPDiscount(DiscountDecorator):
    def calculate_cost(self):
        return self._decorated_purchase.calculate_cost() * 0.8  

# Постоянный клиенттер үшін деконатор
class LoyaltyDiscount(DiscountDecorator):
    def calculate_cost(self):
        return self._decorated_purchase.calculate_cost() * 0.9  

# Консольға статус пен сумманы енгізу
def input_customer_data():
    status = input("Enter your status (regular, VIP, or loyal): ").strip().lower()
    cost = float(input("Enter the purchase amount: "))
    return status, cost

# Статусқа карай баға шығаруға функция
def create_purchase(status, cost):
    purchase = RegularPurchase(cost)
    if status == "vip":
        return VIPDiscount(purchase)  
    elif status == "loyal":
        return LoyaltyDiscount(purchase) 
    elif status == "regular":
        return purchase
    else:
        print("Unknown status, using regular purchase.")
        return purchase


status, cost = input_customer_data()
purchase = create_purchase(status, cost)
discounted_cost = purchase.calculate_cost()

print(f"Total cost for {status} customer: ${discounted_cost:.2f}")
