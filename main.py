import json

Flavours = list[str]
DrinkMenu = dict[str, Flavours]

with open("flavours.json") as f:
    raw_json: dict = json.load(f)

drinks: DrinkMenu = raw_json.get("lemonade") # type: ignore

def flavours(drinks: DrinkMenu) -> set[str]:
    return {flavour for flavour_list in drinks.values() for flavour in flavour_list}

def names(drinks: DrinkMenu) -> set[str]:
    return {drink_name for drink_name in drinks}

drink_names = names(drinks)
drink_flavours = flavours(drinks)


# spaces are replaced with underscores. TODO: document this

def all_flavours_are_valid(flavours: Flavours):
    return all({flavour in drink_flavours for flavour in flavours})

def process(cmd: str) -> None:
    match cmd.lower().split():
        case ["drinks", *flavours] if all_flavours_are_valid(flavours):
            print("Drink is valid")
            pass # print drinks that contain flavour
        case _:
            pass

while True:
    cmd = input("> ")
    process(cmd)
