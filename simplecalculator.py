def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    else:
        return n1 / n2
def main():
    print("Welcome to Simple Calculator")
    while True:
        try:
            n1=float(input("Enter first number: "))
            n2=float(input("Enter second number: "))
            print("\nOperation Choices:")
            print("a. Addition (+)")
            print("b. Subtraction (-)")
            print("c. Multiplication (*)")
            print("d. Division (/)")
            choice = input("Enter your choice (a/b/c/d): ")
            if choice == 'a':
                result = add(n1, n2)
                print(f"\n{n1} + {n2} = {result}")
            elif choice == 'b':
                result = subtract(n1, n2)
                print(f"\n{n1} - {n2} = {result}")
            elif choice == 'c':
                result = multiply(n1, n2)
                print(f"\n{n1} * {n2} = {result}")
            elif choice == 'd':
                result = divide(n1, n2)
                print(f"\n{n1} / {n2} = {result}")
            else:
                print("Invalid choice! Please enter a,b,c or d.")
            another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if another_calculation != 'yes':
                break
        except ValueError:
            print("Error! Please enter valid numbers.")
    print("Thank you for using Simple Calculator. Goodbye!")
if _name_ == "_main_":
    main()