def r_val(n):
    """
    Return the value of a Roman numeral string.
    Handles invalid characters and empty input.
    """
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    if not isinstance(n, str) or not n:
        return "Error: Input must be a non-empty string."

    n = n.upper()
    total = 0
    prev_value = 0

    for char in n:
        if char not in roman_numerals:
            return f"Error: Invalid Roman numeral character '{char}'."
        value = roman_numerals[char]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total

def r_num(n):
    """
    Return the Roman numeral representation of an integer.
    Handles out-of-range and non-integer input.
    """
    if not isinstance(n, int):
        return "Error: Input must be an integer."
    if not (0 < n < 4000):
        return "Error: Input must be between 1 and 3999."

    roman_numerals = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    
    result = []
    for numeral, value in roman_numerals:
        while n >= value:
            result.append(numeral)
            n -= value

    return ''.join(result)

if __name__ == "__main__":
    # Example usage with error handling
    test_cases = [
        "XIV", "MMXXIII", "ABC", "", None, 14, 2023, 4000, -5, "123"
    ]
    print("Roman to Integer:")
    for case in test_cases[:5]:
        print(f"{case}: {r_val(case)}")
    print("\nInteger to Roman:")
    for case in test_cases[5:]:
        print(f"{case}: {r_num(case)}")