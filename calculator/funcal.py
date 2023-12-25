def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def power(n1, n2):
    return n1 ** n2

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '**': power
}

def calculator():
        num1 = float(input('Enter the number : '))

        for symbol in operations:
            print(symbol)

        want_to_continue = True
        while want_to_continue:

            while True:
                operation_symbol = input('Enter the operator: ')
                if operation_symbol in operations:
                    print('valid operations')
                    break
                else:
                    print("Please Enter Valid Operator")
                
            num2 = float(input('Enter the number : '))

            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f'{num1} {operation_symbol} {num2} = {answer}')

            if input(f"Do you wish to continue with {answer} ? Press y for yes and n for no: ") == "y":
                num1 = answer
            else:
                want_to_continue == False
                print('Thank you for using Simple Calculator')
                calculator()
calculator()