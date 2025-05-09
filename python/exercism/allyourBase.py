def rebase(input_base, digits, output_base):
    # for input.
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # another example for input.
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # or, for output.
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    base10 = sum(digit * (input_base ** i) for i, digit in enumerate(reversed(digits)))
    if base10 == 0:
        return [0]
    converted_to_op_base = []
    while base10 != 0:
        converted_to_op_base.insert(0, base10 % output_base)
        base10 //= output_base

    return converted_to_op_base

print(rebase(0, [], 10))
