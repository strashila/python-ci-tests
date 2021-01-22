# Function that returns arabic number for roman number input

def roman_to_arabic(roman_num):
    arabic_num = 0
    special_char_dict = {
        "IV": 4,
        "XL": 40,
        "CD": 400,
        "IX": 9,
        "XC": 90,
        "CM": 900
    }

    regular_char_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for key in special_char_dict:
        if key in roman_num:
            arabic_num += special_char_dict[key]
            roman_num = roman_num.replace(key, "")

    for roman_char in roman_num:
        arabic_num += regular_char_dict[roman_char]

    return arabic_num


# removed comments and placeholder for arabic to roman func

