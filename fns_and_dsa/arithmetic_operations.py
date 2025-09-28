num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
opearation = input("Enter operation(add,subtract,multiply,divide)")


def perform_operation():
    if opearation == "add":
        result = num1 + num2
        print("Result :",result)
    if opearation == "subtract":
        result = num1 - num2
        print("Result :",result)
    if opearation == "multiply":
        result = num1 * num2
        print("Result :",result)
    if opearation == "divide":
        if num2 ==0:
            result = "Not divisiable"
            print("Result :",result)
        else:
            result = num1/num2
            print("Result :", result)


