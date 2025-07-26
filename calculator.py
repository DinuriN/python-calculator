import sys

def add (a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if(b==0):
        raise ValueError("Cannot divide by 0")
    return a/b

if __name__=="__main__":
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <a> <b>")
        sys.exit(1)

    operation, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation in operations:
        try:
            print("Answer: ", operations[operation](a,b))
        except ValueError as e:
            print(e)
    else:
        print("Invalid Operation. Try again")