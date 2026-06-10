
class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    ## function for verifying if a sandwich is able to be made.
    def check_resources(self, order_ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount_needed in order_ingredients.items():
            if amount_needed > self.resources[ingredient]:
                return False

        return True

    ## will remove the ingredients from the resources dictionary
    def make_sandwich(self, order_ingredients):
        """Deduct the required ingredients from the resources.
            Hint: no output"""
        for ingredient, amount_needed in order_ingredients.items():
            self.resources[ingredient] -= amount_needed