num1 = int(input("Enter the first number...\n"))
num2 = int(input("Enter the second number...\n"))

if num2<num1:
	mn = num1
else:
	 mn = num2 
	
for i in range(1,mn+1):
		hcf=i
		
print("\n")
print("Bigger number is -")
print(hcf)