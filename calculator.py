def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def main():
    a = float(input("First number: "))
    op = input(f"Operation {list(OPERATIONS)}: ")
    b = float(input("Second number: "))
    print("Result:", OPERATIONS[op](a, b))

if __name__ == "__main__":
    main()