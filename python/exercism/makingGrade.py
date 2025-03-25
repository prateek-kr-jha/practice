
def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    return sum(score <= 40 for score in student_scores)

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    divison = (highest - 40) // 4
    return list(range(41, highest, divison))


def is_isogram(string):
    phrase_breakup = {}

    for char in string:
        if char.isalpha():
            if phrase_breakup.get(char):
                return False
            else:
                phrase_breakup[char] = 1

    return True



    print(phrase_breakup)


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = [num for num in range (1, number) if number % num == 0]
    aliquot_sum = sum(factors)
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"


# def to_rna(dna_strand):
    # map = {
    #     "A": "U",
    #     "C": "G",
    #     "T": "A",
    #     "G": "C"
    # }
    # return "".join([map[char] for char in dna_strand])

LOOKUP = str.maketrans("GCTA", "CGAU")
print(LOOKUP)

def to_rna(dna_strand):
    return dna_strand.translate(LOOKUP)



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
def color_code(color):
    return LOOKUP.index(color)


def colors():
    return LOOKUP


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    # factors = [num for num in range (1, number) if number % num == 0]
    factors = {1}
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            factors.add(num)
            if number // num != num:
                factors.add(number // num)
    aliquot_sum = sum(factors)

    return "deficient" if aliquot_sum < number else "perfect" if aliquot_sum == number else "abundant"

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


def label(colors):
    resistor_value = (LOOKUP[colors[0]] * 10 + LOOKUP[colors[1]]) * 10 ** LOOKUP[colors[2]]

    return f"{resistor_value if resistor_value < 1000 else resistor_value // 1000} {"ohms" if resistor_value < 1000 else "kiloohms"}"

print(label(["red", "black", "red"]))
