FAHRENHEIT_TO_CELSIUS_FACTOR = globals
CELSIUS_TO_FAHRENHEIT_FACTOR = globals

degree = int(input("Enter temperature :"))
temp = input("is the temperature(celsius, fahrenheit) :")

if temp =="celsius":
    def convert_to_fahrenheit ():
     new_temp = degree * CELSIUS_TO_FAHRENHEIT_FACTOR
print("The temperature in fanhrenheit is :",new_temp) # pyright: ignore[reportUndefinedVariable]
if temp == "fahrenheit":
    def convert_to_celsius():
     new_temp = degree * FAHRENHEIT_TO_CELSIUS_FACTOR
    print("The temperature in celsius is :",new_temp) # pyright: ignore[reportUndefinedVariable]
else:
   print("invalid input")