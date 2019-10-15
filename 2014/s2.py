f = open("s2.5b.in", "r")
if int(f.readline()) % 2 == 1:
	print("bad")
else:
	first_partners_str = f.readline()
	first_partners = first_partners_str.split()

	second_partners_str = f.readline()
	second_partners = second_partners_str.split()

	bad = False

	for i in range(len(first_partners)):
		for j in range(len(second_partners)):
			if first_partners[i] == second_partners[i]:
				print("bad")
				bad = True
				break
			if first_partners[i] == second_partners[j]:
				if second_partners[i] == first_partners[j]:
					break
				print("bad")
				bad = True
				break
			
		if bad == True:
			break
		
	if bad == False:
		print("good")

	

