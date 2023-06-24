import json

with open("flavours.json") as f:
    raw_json: dict = json.load(f)

flavours = raw_json.get("LEMONADE")

def process(cmd: str) -> None:
    match cmd.upper():
        case _:
            pass

while True:
    cmd = input("> ")
