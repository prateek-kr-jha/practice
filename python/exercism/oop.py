def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for i in range(number):
        yield chr(ord('A') + (i % 4))
        # letter  = chr(int(letter, 16) + 1)


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = generate_seat_letters(number)
    i = 1
    for letter in seat_letters:
        if i == 13:
            i += 1
        yield f"{i}{letter}"
        if letter == "D":
            i += 1


        

seats = generate_seats(14 * 4)

# ["1A", "1B", "1C", "1D", "2A"]
# print(next(seats))
# for seat in seats:
#     print(seat)


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield f"{seat}{flight_id}".ljust(12, '0')

