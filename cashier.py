from readline import insert_text


class Cashier:
    def __init__(self):
        pass

    # function for adding coins to machine
    def process_coins(self):
        """Returns the total calculated from coins inserted.
            Hint: include input() function here, e.g. input("how many quarters?: ")"""

        # indefinite loop to continue trying for numerical input
        while True:
            try:
                dollars = float(input("Enter the amount of large dollars"))
                half_dollars = float(input("Enter the amount of half dollars"))
                quarters = float(input("Enter the amount of quarters"))
                nickels = float(input("Enter the amount of nickels"))
                break

            # throw value error if input is not numerical
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        total = dollars + (.5 * half_dollars) + (.25 * quarters) + (.05 * nickels)
        print(f'You added ${total:.2f} worth of coins.')
        return total

    # function that returns a result which is bool, and coins or change which is float
    def transaction_result(self, inserted_coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
            Hint: use the output of process_coins() function for cost input"""
        if inserted_coins < cost:
            return False, inserted_coins
        else:
            change = inserted_coins - cost
            return True, change
