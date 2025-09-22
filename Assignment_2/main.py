import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# creating instances of classes
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True
    while is_on:
        user_choice = input("what would you like? (small/medium/large/off/report): ").lower()

        if user_choice == "off":
            is_on = False
        elif user_choice == "report":
            # show current resource levels
            print(f"bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"cheese: {sandwich_maker_instance.machine_resources['cheese']} ounces(s)")
        elif user_choice in recipes:
            sandwich = recipes[user_choice]
            # check resources, process payment, make the sandwich if everything is good
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                # make sure payment is not 0 from invalid input
                if payment > 0 and cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(user_choice, sandwich["ingredients"])
        else:
            print("invalid choice. please try again.")

if __name__ == "__main__":
    main()