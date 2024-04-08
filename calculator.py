print('''
	1.Addition
	2.Subtraction
	3.Multiplication
	4.Division
	5.Square
	''')
num1=int(input("Enter the first value:"))
num2=int(input("Ënter the second value:"))
opr=input("Enter the operator.....(+, -, *, /)")
if opr=="+":
		print(num1+num2)
elif opr=="-":
		print(num1-num2)
elif opr=="*":
		print(num1*num2)
elif opr=="/":
		print(num1/num2)
elif opr=="**":
	print(num1**num2)
else:
		print("Invalid operator......")