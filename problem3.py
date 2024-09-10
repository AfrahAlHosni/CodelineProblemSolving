def right_angle_triangle_choise(n):
    for a in range(1, n + 1):
        print('1 ' * a)

def palindromic_triangle_choise(n):
    for x in range(1, n + 1):
        
        print(' ' * (n - x))
        
        for y in range(1, x + 1):
            print(y, end='')
        
        for y in range(x - 1, 0, -1):
            print(y, end='')
        print()

def helpChoise():
    print("\nHelp:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome. The first few lines of a Palindromic Triangle are:")
    print("1\n 11 \n 121 \n 12321 \n 1234321 ")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.\n")

# ******Munu
def main():
    while True:
        print("Menu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        menu = input("Enter your choice (1-4): ")
        
        if menu == '1':
            try:
                n = int(input("Enter the number of lines: "))
                if n > 0:
                    right_angle_triangle_choise(n)
                else:
                    print("Number of rows should be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif menu == '2':
            try:
                n = int(input("Enter the number of lines: "))
                if n > 0:
                    palindromic_triangle_choise(n)
                else:
                    print("Number of rows must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif menu == '3':
            helpChoise()
        
        elif menu == '4':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
