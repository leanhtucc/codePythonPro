for i in range(7):
	for j in range(7):
		if i == 0 and j in (1, 2, 4, 5):
			print("*",end="  ")
		elif i == 1 and j in (0, 3, 6):
			print("*",end="  ")
		elif i == 2 and j in (0, 6):
			print("*",end="  ")
		elif i == 3 and j in (1, 5):
			print("*",end="  ")
		elif i == 4 and j in (2, 4):
			print("*",end="  ")
		elif i == 5 and j == 3 :
			print("*",end="  ")
		else:
			print(" ",end="  ")

	print()

