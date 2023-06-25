import json

from customtypes import Flavours, DrinkMenu

with open("flavours.json") as f:
    raw_json: dict = json.load(f)

drinks: DrinkMenu = raw_json.get("lemonade")  # type: ignore


def flavours(drinks: DrinkMenu) -> set[str]:
    """### Parameters
    - :param `DrinkMenu` `drinks`:

    ### Returns
    :return: All unique flavours from all the drinks on the menu.
    :rtype: `set[str]`
    """
    return {flavour for flavour_list in drinks.values() for flavour in flavour_list}


def names(drinks: DrinkMenu) -> set[str]:
    """### Parameters
    - :param `DrinkMenu` `drinks`:

    ### Returns
    :return: All drink names on the menu.
    :rtype: `set[str]`
    """
    return {drink_name for drink_name in drinks}


DRINK_NAMES = names(drinks)
DRINK_FLAVOURS = flavours(drinks)


# spaces are replaced with underscores. TODO: document this


def all_flavours_are_valid(flavours: Flavours):
    return all({flavour in DRINK_FLAVOURS for flavour in flavours})


def process(cmd: str) -> None:
    match cmd.lower().split():
        case ["drinks", *flavours] if all_flavours_are_valid(flavours):
            print("Drink is valid")
            pass  # print drinks that contain flavour
        case _:
            pass


while True:
    cmd = input("> ")
    process(cmd)
