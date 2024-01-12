def hex_to_decimal(hex_string):
    decimal_integer = int(hex_string, 16)
    decimal_string = str(decimal_integer)
    return decimal_string


# Example usage:
hex_string = "1a"  # Replace this with your hexadecimal string
decimal_string = hex_to_decimal(hex_string)
print(f"The decimal representation of {hex_string} is: {decimal_string}")
