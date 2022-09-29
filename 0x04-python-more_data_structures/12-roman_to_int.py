#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    i = 0
    roman = 0
    if isinstance(roman_string, str):
        for i in range(len(roman_string) - 1):
            if roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
                roman = roman + roman_dict[roman_string[i]]
            else:
                roman = roman - roman_dict[roman_string[i]]
            i = i + 1
        roman = roman + roman_dict[roman_string[i]]
        return (roman)
    else:
        return (0)
