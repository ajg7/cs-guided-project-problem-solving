"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str: str) -> str:
    # Your code here
    str_digits = input_str.split(" ")
    int_digits = []
    
    for str_digit in str_digits:
        int_digit = int(str_digit)
        int_digits.append(int_digit)
        
    mx = max(int_digits)
    mn = min(int_digits)
    
    return f"{mx} {mn}"

