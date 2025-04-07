LOOKUP = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

PREFIX_LOOKUP = {
    3: "kiloohms",
    6: "megaohms",
    9: "gigaohms",
}


def label(colors):
    if len(colors) < 3:
        raise ValueError("At least three colors are required")

    resistor_value = (LOOKUP[colors[0]] * 10 + LOOKUP[colors[1]]) * (10 ** LOOKUP[colors[2]])

    for exponent in sorted(PREFIX_LOOKUP.keys(), reverse=True):
        factor = 10 ** exponent
        if resistor_value >= factor:
            value = resistor_value / factor
            value_str = f"{value:.1f}".rstrip("0").rstrip(".")
            return f"{value_str} {PREFIX_LOOKUP[exponent]}"
    
    return f"{resistor_value} ohms"


print(label(["red", "orange", "yellow"]))