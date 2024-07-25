def hex_to_decimal(hex_number):
    """
    Convert a hexadecimal number to decimal.

    Parameters:
    hex_number (str): A string representing a hexadecimal number (e.g., '0x1a2b3c').

    Returns:
    int: The decimal representation of the hexadecimal number.
    """
    try:
        # Convert the hexadecimal number to decimal
        decimal_number = int(hex_number, 16)
        return decimal_number
    except ValueError:
        # Handle the case where the input is not a valid hexadecimal number
        print("Invalid hexadecimal number")
        return None

if __name__ == "__main__":
    # Example usage
    hex_number_1 = "0x2ff8e680622e87714541ec83c95d69a9a2a719403380a3bb04e33406fb25f2a6"
    hex_number_2 = "0x039c5de593566f6834a3c26699aa7cbb7450b11d9e08c077037e5c366bc5d96f"

    decimal_number_1 = hex_to_decimal(hex_number_1)
    decimal_number_2 = hex_to_decimal(hex_number_2)

    print(f"The decimal equivalent of {hex_number_1} is {decimal_number_1}")
    print(f"The decimal equivalent of {hex_number_2} is {decimal_number_2}")

