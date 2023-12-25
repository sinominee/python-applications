# Addition
def add(n1, n2):
    return n1 + n2
# Subtraction
def sub(n1, n2):
    return n1 - n2
# Multiplication
def mul(n1, n2):
    return n1 * n2
# Divide
def div(n1, n2):
    return n1 / n2
#modulus
def mod(n1, n2):
    return n1 % n2
# power exponentiation
def power(n1, n2):
    return n1 ** n2
# floor  division
def floor(n1, n2):
    return n1 // n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": mod,
    "**": power,
    "//": floor
}

def calcuator():
    num1 = float(input("What is the First Number: "))   
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the Second Number: "))   
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' if you want to calculate with {answer}: or 'n' to start a new: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calcuator()
            
calcuator()


# should_end = False
# while not should_end:

    # num1 = int(input("What is the First Number: "))   
    # for symbol in operations:
    #     print(symbol)
    # operation_symbol = input("Pick an operation: ")
    # num2 = int(input("What is the Second Number:"))   
    # calculation_function = operations[operation_symbol]
    # first_answer = calculation_function(num1, num2)
    # print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    # operation_symbol = input("Pick an operation:")
    # num3 = int(input("What is the next Number:"))
    # calculation_function = operations[operation_symbol]
    # second_answer = calculation_function(first_answer, num3)             
    # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# cont = input(f"Type 'y' if you want to calculate with {first_answer}, otherwise 'n' to exit.")
#     if cont == "y":
#         should_end = True
    
