# calculator.py

def calculator():
    print("*** Welcome to Calculator ***") 
    print("Created by Guru")
    print("-" * 40)
    
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("Choose operation:")
        print(" + for Addition")
        print(" - for Subtraction")
        print(" * for Multiplication")
        print(" / for Division")
        print(" % for Modulo")
        print(" // for Floor Division")
        print(" ** for Exponentiation")

        operator = input("Enter operator: ")

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b != 0:
                result = a / b
            else:
                return "Error: Division by zero!"
        elif operator == "%":
            result = a % b
        elif operator == "//":
            result = a // b
        elif operator == "**":
            result = a ** b
        else:
            return "Invalid operator!"

        return f"The result of {a} {operator} {b} is: {result}"
    except ValueError:
        return "Invalid input! Please enter numeric values."

if __name__ == "__main__":
    output = calculator()
    print(output)
