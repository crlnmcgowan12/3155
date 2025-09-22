class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """returns true if the sandwich can be made, false if not."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """deducts ingredients from the machine's resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. bon appetit!")