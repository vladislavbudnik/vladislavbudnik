print("Ноль в качестве знака операции завершит работу программы")
while True:
	s = int(input("Знак (1-xor, 2-and, 3-not, 4-or): "))
	if (s < 1 or s > 4): break
	elif (s >= 1 or s <= 4):
		x = float(input("x="))
		y = float(input("y="))
		if (s == 1):
			print("%.2f" % (int(x) ^ int(y)))
		elif (s == 2):
			print("%.2f" % (x and y))
		elif (s == 3):
			print("%.2f" % (x != y))
		elif (s == 4):
			print("%.2f" % (x or y))
