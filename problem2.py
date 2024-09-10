# ****** Convert decimal number to binary ****

def convert_decimal_to_binary(x):
    if x <= 0:
        return "please the entered a number, must be a positive ."
    
    binary_numbers = []
    
    while x > 0:
        rest = x % 2
        binary_numbers.append(str(rest))
        n = n // 2
    
   
    binary_numbers.reverse()
    
   
    binary_chars = ''.join(binary_numbers)
    return binary_chars

def main():
    try:
        decimal_number = int(input(" Please enter a positive decimal number: "))
        
        if decimal_number < 0:
            print("Please enter a positive number.")
            return
        
        binary_equivalent = convert_decimal_to_binary(decimal_number)
        print(f"The binary equivalent of {decimal_number} is {binary_equivalent}.")
    
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
