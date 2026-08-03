print("                                          Mini Calculator                                                   ")


a = int(input("Enter Number = "))
b = input("Enter Operator = ")
c = int(input("Enter Number = "))


if b == "+":
    print("Your Answers is = ",(a + c))
elif b=="-":
    print("Your Answer is = " ,(a - c))
elif b=="*":
    print("Your Answer is = " ,(a * c))
elif b=="/":
    print("Your Answer is = " ,(a / c))
else:
    print("Invalid Operations")    