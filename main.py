from Exception import invalid_choice

from Pet_shop import Zoo
import logging
import sys
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")
petshop = Zoo()
animals = []
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
while True:

    print("1.Add Lion.")
    print("2.Add Parrot")
    print("3.Add Fish")
    print("4.Lion methods")
    print("5.Parrot methods")
    print("6.Fish methods")
    print("7.Remove")
    print("8.Display")
    print("9.Exit")
    while True:
        try:
            choice = input("Input what u want: ")
            if choice.isdigit():
                choice = int(choice)
                if choice <= 0 or choice > 8:
                    logger.error("It has to be between 1-8")
                    raise invalid_choice
                break
            else:
                logger.error("It has to be be a number")
                raise invalid_choice
        except invalid_choice:
            print("Enter a valid choice.")

    match choice:
        case 1:
            petshop.add_lion(animals)
        case 2:
            petshop.add_parrot(animals)
        case 3:
            petshop.add_fish(animals)
        case 4:
            petshop.lion_methods(animals)
        case 5:
            petshop.parrot_methods(animals)
        case 6:
            petshop.fish_methods(animals)
        case 7:
            petshop.delete_animal(animals)
        case 8:
            petshop.print_available(animals)
        case 9:
            break
