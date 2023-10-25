def subtract_numbers(num1, num2):
    return num1 - num2

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = subtract_numbers(num1, num2)
    print(f"The subtraction of {num1} and {num2} is {result}")

if __name__ == '__main__':
    main()
