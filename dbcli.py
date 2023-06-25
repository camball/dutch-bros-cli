import json
from string import capwords
from typing import Iterable

from customtypes import Flavours, DrinkMenu

with open("flavours.json") as f:
    raw_json: dict = json.load(f)

DRINKS: DrinkMenu = raw_json.get("lemonade")  # type: ignore

DRINK_NAMES = {drink_name for drink_name in DRINKS}
"""All drink names on the menu."""

DRINK_FLAVOURS = {flavour for flavours in DRINKS.values() for flavour in flavours}
"""All unique flavours from all the drinks on the menu."""


def underscores_to_spaces(strings: Iterable[str]) -> set[str]:
    return set(map(lambda string: string.replace("_", " "), strings))


def all_flavours_in_flavour_list(flavours_to_check: Flavours, flavour_list: Flavours):
    flavours_to_check = underscores_to_spaces(flavours_to_check)
    return all({flavour in flavour_list for flavour in flavours_to_check})


def all_flavours_are_valid(flavours: Flavours):
    return all_flavours_in_flavour_list(flavours, DRINK_FLAVOURS)


def is_valid_flavour(flavour: str):
    return flavour.replace("_", " ") in DRINK_FLAVOURS


def is_valid_drink(drink_name: str):
    return drink_name.replace("_", " ") in DRINK_NAMES


def _print_invalid_flavours(flavours: Flavours):
    for flavour in flavours:
        if flavour not in DRINK_FLAVOURS:
            print(f"{capwords(flavour)} is not a valid flavour.")


def _print_drink(drink_name: str, flavours_not_passed: Flavours) -> None:
    if flavours_not_passed:
        formatted_flavours = str()
        for idx, flav in enumerate(flavours_not_passed):
            if idx != 0:
                formatted_flavours += ","
            formatted_flavours += f" {capwords(flav)}"
        print(f"{capwords(drink_name)}:{formatted_flavours}")
    else:
        print(capwords(drink_name))


def process(cmd: str) -> None:
    match cmd.lower().split():
        case ["quit" | "exit"]:
            exit()
        case ["flavours"]:
            for flavour in sorted(DRINK_FLAVOURS):
                print(capwords(flavour))
        case ["drinks", *flavours, "except", flavour_to_exclude]:
            if not all_flavours_are_valid(flavours):
                _print_invalid_flavours(flavours)
                return

            if not is_valid_flavour(flavour_to_exclude):
                print(
                    f'"{flavour_to_exclude}" is not a flavour, so it can\'t be excluded...'
                )
                print("Here's the drinks with the ones you mentioned anyway:\n")

            for drink_name, drink_flavours in DRINKS.items():
                if (
                    all_flavours_in_flavour_list(flavours, drink_flavours)
                    and flavour_to_exclude not in drink_flavours
                ):
                    flavours_not_passed = set(drink_flavours).difference(
                        underscores_to_spaces(flavours)
                    )
                    _print_drink(drink_name, flavours_not_passed)
        case ["drinks", *flavours]:
            if not all_flavours_are_valid(flavours):
                _print_invalid_flavours(flavours)
                return

            for drink_name, drink_flavours in DRINKS.items():
                if all_flavours_in_flavour_list(flavours, drink_flavours):
                    flavours_not_passed = set(drink_flavours).difference(
                        underscores_to_spaces(flavours)
                    )
                    _print_drink(drink_name, flavours_not_passed)
        case [drink] if is_valid_drink(drink):
            for flavour in DRINKS.get(drink.replace("_", " "), list()):
                print(capwords(flavour))
        case _:
            pass


def run_shell() -> None:
    while True:
        cmd = input("> ")
        print()
        process(cmd)
        print()


run_shell()
