def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    print("\n--- Basic Calculator ---")

    num1 = get_number("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ")
    num2 = get_number("Enter second number: ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print("Result:", result)


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    choice = input("Enter your choice: ")

    if choice == "1":
        km = get_number("Enter distance in kilometers: ")
        miles = km * 0.621371
        print("Distance in miles:", miles)

    elif choice == "2":
        miles = get_number("Enter distance in miles: ")
        km = miles / 0.621371
        print("Distance in kilometers:", km)

    elif choice == "3":
        celsius = get_number("Enter temperature in Celsius: ")
        fahrenheit = (celsius * 9 / 5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

    elif choice == "4":
        fahrenheit = get_number("Enter temperature in Fahrenheit: ")
        celsius = (fahrenheit - 32) * 5 / 9
        print("Temperature in Celsius:", celsius)

    else:
        print("Invalid choice!")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("1. INR to USD")
    print("2. USD to INR")
    print("3. INR to EUR")
    print("4. EUR to INR")

    choice = input("Enter your choice: ")

    # Example fixed rates for the assignment
    INR_TO_USD = 0.0119
    USD_TO_INR = 84.00
    INR_TO_EUR = 0.0101
    EUR_TO_INR = 99.00

    if choice == "1":
        inr = get_number("Enter amount in INR: ")
        print("Amount in USD:", inr * INR_TO_USD)

    elif choice == "2":
        usd = get_number("Enter amount in USD: ")
        print("Amount in INR:", usd * USD_TO_INR)

    elif choice == "3":
        inr = get_number("Enter amount in INR: ")
        print("Amount in EUR:", inr * INR_TO_EUR)

    elif choice == "4":
        eur = get_number("Enter amount in EUR: ")
        print("Amount in INR:", eur * EUR_TO_INR)

    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n==============================")
        print(" INTERACTIVE CALCULATOR")
        print(" & UNIT CONVERTER")
        print("==============================")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Currency Converter")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            unit_converter()

        elif choice == "3":
            currency_converter()

        elif choice == "4":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
