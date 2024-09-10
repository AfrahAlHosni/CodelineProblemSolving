

def even_numbers_square(squareNumbers):
  
    return [y**2 for y in squareNumbers if y % 2 == 0]

def list_slice(num, start, end):
   
    return num[start:end]

def main():
    try:
        
        input_list = input("please enter a list of integers separated by spaces: ")
        numbers = list(map(int, input_list.split()))
        
        
        print(f"Original list: {numbers}")
        
      
        even_squares = even_numbers_square(numbers)
        print(f"Squares of even numbers: {even_squares}")
        

        start_index = int(input("Enter the start index for slicing: "))
        end_index = int(input("Enter the end index for slicing: "))
        
        
        sublist = list_slice(numbers, start_index, end_index)
        print(f"Sublist from index {start_index} to {end_index}: {sublist}")
    
    except ValueError:
        print("Invalid input. Please enter integers only for the list and indices.")
    except IndexError:
        print("Index out of range. Please ensure your indices are within the bounds of the list.")

if __name__ == "__main__":
    main()
