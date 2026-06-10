import sys

from data import resources as inventory
from data import recipes
from sandwich_maker import SandwichMaker
from cashier import Cashier

""" GITHUB REPO URL: https://github.com/bpooter/Assignment_1.git"""


def main():
    sandwich_machine = SandwichMaker(inventory)
    cashier = Cashier()

    show_menu(sandwich_machine, cashier)


def show_menu(sandwich_machine, cashier):
    print("\nWelcome to the Sandwich Machine!\n")

    ## indefinite loop till off is chosen
    while True:

        ## retrieving user input and shifting to lower case and stripping whitespace
        choice = input("\nWhat would you like? (small/ medium/ large/ off/ report)")
        choice = choice.lower().strip()

        ## match for options chosen off menu
        match choice:

            case "small" | "medium" | "large":

                #fetching ingredients for sandwich that was chosen
                ingredients = recipes[choice]["ingredients"]

                #fetching cost of chosen sandwich
                cost = recipes[choice]["cost"]

                ## checking to see if resources are available first
                if sandwich_machine.check_resources(ingredients):

                    print("\nSure thing we can make that!\n")
                    print(f'Your sandwich will cost ${cost:.2f}\n')

                    ## variable to hold amount of coins added
                    total_added = cashier.process_coins()

                    ## returning 2 values from transaction_result transaction = bool, change = float
                    transaction, change = cashier.transaction_result(total_added, recipes[choice]["cost"])

                    ## if transaction is successful make sandwich deducting from resources
                    if transaction:
                        print(f'We are making the sandwich now!\nHere is your change of ${change:.2f}\n')
                        sandwich_machine.make_sandwich(choice, ingredients)

                        print(f'Your {choice} sandwich is ready! Bon Appetit!!\n')
                    else:
                        print(f'Sorry, that is not enough money. Refunding ${change:.2f} to you\n')

                ## if resources are too low to make a sandwich display message
                else:
                    print("\nSorry, we don't have enough ingredients.\n")

            ## exit the sandwich machine program
            case "off":
                sys.exit(0)


            ## case for report viewing of resources available
            case "report":
                ## show the resources that are available
                for ingredient, quantity in inventory.items():
                    print(ingredient, quantity)

            ## default case for error in main menu
            case _:
                print("You must enter a valid choice from the menu.")

if __name__ == '__main__':
    main()
