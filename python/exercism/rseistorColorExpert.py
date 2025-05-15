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

TOLERANCE_LOOKUP = {
    "grey" : 0.05,
    "violet" : 0.1,
    "blue" : 0.25,
    "green" : 0.5,
    "brown" : 1,
    "red" : 2,
    "gold" : 5,
    "silver" : 10,
}

def resistor_label(colors):
    if len(colors) < 4:
        raise ValueError("At least three colors are required")
    tolerance = None
    resistor_value = None
    if len(colors) == 5:
        resistor_value = (LOOKUP[colors[0]] * 100 + LOOKUP[colors[1]] * 10 + LOOKUP[colors[2]]) * 10 ** LOOKUP[colors[3]]
        tolerance = colors[4]
    else:
        resistor_value = (LOOKUP[colors[0]] * 10 + LOOKUP[colors[1]]) * 10 ** LOOKUP[colors[2]]
        tolerance = colors[3]
    
    value_string = ""
    if resistor_value < 1000:
        value_string = f"{resistor_value} ohms"
    elif resistor_value < 1_000_000:
        value_string = f"{resistor_value / 1_000 + resistor_value % 1_000} kiloohms"
    elif resistor_value < 1_000_000_000:
        value_string = f"{resistor_value / 1_000_000 + resistor_value % 1_000_000} megaohms"
    else:
        value_string = f"{resistor_value / 1_000_000_000} gigaohms"
    return value_string + (f" ±{TOLERANCE_LOOKUP[tolerance]}%" if tolerance else "")



print(resistor_label(["orange", "orange", "black", "red"]))

# if len == 5 multiplir = 4 else 5