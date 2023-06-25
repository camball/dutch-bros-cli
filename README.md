# dutch-bros-cli

## Motivation

### 😧 The Problem

Dutch Bros has too many flavours. But they’re all SO GOOD. Usually there are many flavours that look good but I have to scroll all around the website comparing them and I end up picking one, but only out of fatigue. It’s an issue.

### 😌 The Solution

The Dutch Bros flavour picker: a CLI for picking for drinks based on the their flavours, seeing all flavours, and the flavours in any drink. Say you *know* you want Raspberry in your drink. No time to sift through the scattered website in line! Using this tool you quickly discover that your options are down to Astronaut, Dragon Slayer, Gem Berry, and Laser Cat, and you can quickly see the differences between them so you can make the most informed choice 😄.

## Installation

```sh
git clone https://github.com/camball/dutch-bros-cli
cd dutch-bros-cli
python3 -m dbcli
```

## Usage

- List all the drinks with the specified flavours

    ```txt
    > drinks Coconut

    Laser Cat: Raspberry
    Rocky Point: Blackberry, Orange, Peach
    Tiger's Blood: Strawberry
    ```

    > Note: Anywhere you'd ordinarily have a space in a flavour or drink name, an underscore must be used instead, such as in the following:

    ```txt
    > drinks Passion_Fruit Pomegranate

    Hyperchrome: Orange
    Og Gummybear: Watermelon, Grapefruit
    Palm Tree: Lime
    Stop Light: Kiwi
    ```

- List all the drinks with the specified flavours, excluding all drinks that have Orange in them

    ```txt
    > drinks Passion_Fruit Pomegranate except Orange

    Og Gummybear: Watermelon, Grapefruit
    Palm Tree: Lime
    Stop Light: Kiwi
    ```

- List all flavours

    ```txt
    > flavours

    Almond
    Banana
    Blackberry
    Blackberry Drizzle
    Blue Raspberry
    …
    ```

- List all flavours in a drink

    ```txt
    > Aquaberry

    Strawberry
    Kiwi
    Blue Raspberry
    Watermelon
    ```

- Find the closest Dutch Bros to you

    ```txt
    > find

    {address}
    ```

- Exit the program

    ```txt
    > {exit | quit}
    ```

---

Flavours from <https://www.dutchbros.com/menu/lemonade>
