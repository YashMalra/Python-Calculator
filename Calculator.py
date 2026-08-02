print("                                          Mini Calculator                                                   ")


a = int(input("Enter Number = "))
b = input("Enter Operator = ")
c = int(input("Enter Number = "))


if b == "+":
    print("KUCHU PUCHU Your Answers is = ",(a + c))
elif b=="-":
    print("KUCHU PUCHU Your Answer is = " ,(a - c))
elif b=="*":
    print("KUCHU PUCHU Your Answer is = " ,(a * c))
elif b=="/":
    print("KUCHU PUCHU Your Answer is = " ,(a / c))
else:
    print("Invalid Operations")    