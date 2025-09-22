class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """returns the total value of coins the user inserted."""
        print("please insert coins.")
        try:
            total = float(input("how many large dollars?: ")) * 1.00
            total += float(input("how many half dollars?: ")) * 0.50
            total += float(input("how many quarters?: ")) * 0.25
            total += float(input("how many nickels?: ")) * 0.05
            return total
        except ValueError:
            print("invalid input. money refunded.")
            return 0  # return 0 for failed transaction

    def transaction_result(self, coins, cost):
        """returns true if the payment is enough, false otherwise."""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"here is ${change} in change.")
            return True
        else:
            print("sorry that's not enough money. money refunded.")
            return False