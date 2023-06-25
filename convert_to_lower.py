"""Utility script for converting uppercase from Dutch Bros website to lower."""
import json
from customtypes import DrinkMenu

with open("flavours.json") as i:
    raw_json: dict = json.load(i)

drinks: DrinkMenu = raw_json.get("lemonade")  # type: ignore

lowercase_drinks: DrinkMenu = dict()
for name, flavour_list in drinks.items():
    lowercase_drinks[name.lower()] = [flavour.lower() for flavour in flavour_list]

raw_json["lemonade"] = lowercase_drinks

with open("flavours.json", "w") as o:
    o.write(json.dumps(raw_json, indent=4))
