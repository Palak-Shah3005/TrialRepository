def square_number(num):
    return num ** 2

def main():
    user_input = float(input("Enter a number: "))
    result = square_number(user_input)
    print("The square of the number is:", result)

# Run the program
main()
