print("             SIMPLE CALCULATOR          ")

want_to_continue = True

while want_to_continue is True:
    num1 = float(input("Enter the First number: "))
    valid_operator = ['+', '-', '*', '/', '**']
    while True:
        print(valid_operator)
        operator = input("Enter The Operator: ")
        if operator in valid_operator:
            break
        print("Please Enter Valid Operator: ")
    num2 = float(input("Enter the Second Number: "))

    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "**":
        print(num1**num2)
    
    want_to_continue = input("Do you wish to continue? Press y for yes and n for no: ") == "y"
else:
    want_to_continue == False
    print('Thank you for using Simple Calculator')


    
    


        
    




