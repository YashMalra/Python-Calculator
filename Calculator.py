print("Mini Calculator")


a = int(input("Enter Number = "))
b = input("Enter Operator = ")
c = int(input("Enter Number = "))


if b == "+":
    print(a + c)
elif b=="-":
    print(a - c)
elif b=="*":
    print(a * c)
elif b=="/":
    print(a / c)