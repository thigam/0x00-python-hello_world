#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    sum = 0
    for i in range(len(roman_string) - 1):
        if roman_string[i] == 'M':
            sum += 1000
        elif roman_string[i] == 'D':
            sum += 500
        elif roman_string[i] == 'C':
            if roman_string[i + 1] == 'D' or roman_string[i + 1] == 'M':
                sum -= 100
            else:
                sum += 100
        elif roman_string[i] == 'L':
            sum += 50
        elif roman_string[i] == 'X':
            if roman_string[i + 1] == 'L' or roman_string[i + 1] == 'C':
                sum -= 10
            else:
                sum += 10
        elif roman_string[i] == 'V':
            sum += 5
        elif roman_string[i] == 'I':
            if roman_string[i + 1] == 'X' or roman_string[i + 1] == 'V':
                sum -= 1
            else:
                sum += 1
    if roman_string[-1] == 'M':
        sum += 1000
    if roman_string[-1] == 'D':
        sum += 500
    if roman_string[-1] == 'C':
        sum += 100
    if roman_string[-1] == 'L':
        sum += 50
    if roman_string[-1] == 'X':
        sum += 10
    if roman_string[-1] == 'V':
        sum += 5
    if roman_string[-1] == 'I':
        sum += 1
    return sum

