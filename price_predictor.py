import numpy as np
#equation to use:  estimatePrice(mileage) = theta0 + (theata1 * mileage)
#set theta0 and theta1 to 0

try:
	while True:
		try:
			mileage = float(input("Enter your mileage: "))
			if (mileage > 0):
				break
			print("Only positive numbers")
		except ValueError:
			print("Invalid arguement, only numbers accepted")

	

except:
	print("Invalid car price")