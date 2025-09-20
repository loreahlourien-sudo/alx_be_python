
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
operation = input ("Choose the operation (+, -, *, /):")

match(operation):
 case"+":
    result = number1 + number2
 case"-":
   result = number1 - number2
 case"*":
    result = number1 * number2
 case"/":
    if number2 == "0" 
    result ="Cannot divide by zero." 
result = number1 / number2
print("The result is",result)

