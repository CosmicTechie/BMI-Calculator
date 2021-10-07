Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("Your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=18.5):
		print("Oops! You are underweight.")
	elif(BMI<=24.9):
		print("Awesome! You are healthy.")
	elif(BMI<=29.9):
		print("You are overweight.")
	else: print("You are Obese. Start Exercise.")
else:("Enter Valid Details")