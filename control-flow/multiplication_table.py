number = int(input("Enter a number to see its multiplication table:"))
x = 1
count = 0
for count in range(1,9) :
 answer = number * x
 print(number,"*" , x,"=" ,answer)
x = x + 1
count = count + 1
