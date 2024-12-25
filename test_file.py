def validate_digit_sequence(s):
    valid_lengths = {13, 16, 18, 19}
    digits = s.split()

    if len(digits) not in valid_lengths:
        return False

    for digit in digits:
        if not digit.isdigit():
            return False

    return True

print(validate_digit_sequence('1 2 3 4 5 6 7 8 9 10 11 12 13'))
