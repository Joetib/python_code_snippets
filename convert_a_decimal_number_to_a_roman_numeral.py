# To convert a decimal number to a roman numeral, we can use a simple algorithm.
# We create a dictionary that maps decimal numbers to their corresponding roman numerals.
# Then, we iterate through the dictionary in descending order of decimal numbers.
# We divide the given decimal number by the current decimal value and append 
# the corresponding roman numeral to the result. We subtract the decimal value multiplied 
# by the quotient from the given decimal number. Finally, we return the result.

def decimal_to_roman(decimal):
    roman_numerals = {
        1000: "M", 900: "CM",500: "D", 400: "CD", 100: "C", 90: "XC", 
        50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I",}
    result = ""
    for value, numeral in roman_numerals.items():
        quotient = decimal // value
        result += numeral * quotient
        decimal -= value * quotient
    return result
# Example usage
decimal = int(input("Enter a decimal number: "))
print(decimal_to_roman(decimal))
# Example output
# Enter a decimal number: 123
# Output >> CXXIII
# Please Like and Subscribe