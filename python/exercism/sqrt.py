# using N-R method
def square_root(number):
    error_value = 1e-6
    assumed_root = number / 2
    while abs(assumed_root ** 2 - number) > error_value:
        assumed_root = (assumed_root + number / assumed_root) / 2

    return assumed_root






def is_pangram(sentence):
    # sentence_set = set(sentence.lower()
    arr = [c for c in sentence if c.isalpha()]
    print(arr)
    sentence_set = set(arr)
    return len(sentence_set) == 26

# print(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"))

"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[-1]



def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return convert_coordinate(azara_record[-1]) == rui_record[1]


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    return (azara_record + rui_record) if compare_records(azara_record, rui_record) else "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    cleaned_record = ""
    for x in combined_record_group:
       cleaned_record += f"('{x[0]}', '{x[2]}', {x[3]}, '{x[-1]}')\n"

    return cleaned_record



def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = dict()
    for item in items:
        if inventory.get(item, False):
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return tuple((key, value)for key, value in inventory.items() if value > 0)
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
