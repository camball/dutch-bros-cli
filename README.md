# dutch-bros-cli

## Problem

Dutch Bros has too many flavours. but they’re all SO GOOD. usually there are many flavours that look good but i have to scroll all around the UI comparing them and i end up picking one, but out of fatigue. it’s an issue.

## Solution

The dutch bros flavour picker. a command line program that exposes operators for comparing and contrasting flavours. e.g.,

```txt
> drinks Coconut
Laser Cat
Tiger’s Blood
Rocky Point
…
```

```txt
> drinks PassionFruit Pomegranate
Palm Tree
Stop Light
…
```

```txt
> drinks {-i | --ingredients} Coconut
Laser Cat {list of ingrendients, minus Coconut (minus the list of ingredients specified, to show the difference. formatted as a nice table.}
Tiger’s Blood {list}
Rocky Point {list}
…
```

```txt
> flavours
Strawberry, Kiwi, Blue Raspberry, Watermelon, Blackberry, Raspberry, Almond, … (list all flavours)
```

```txt
> DragonSlayer - GemBerry
Raspberry # set difference
# internally, that should just be an operator implemented that returns a FlavourList, that could be passed as the input to another command, like drinks DragonSlayer - GemBerry
```

```txt
> AquaBerry
Strawberry, Kiwi, Blue Raspberry, Watermelon # list the flavours
```

```txt
> find # print the closest dutch bros to your current location
{address}
```

---

Flavours from <https://www.dutchbros.com/menu/lemonade>
