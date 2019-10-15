f = open("s1.5.in", "r")
guests_num_str = f.readline()
guests_num = int(guests_num_str)
guests_list = [0] * guests_num

for i in range(guests_num):
	guests_list[i] = i + 1

rounds_str = f.readline()
rounds = int(rounds_str)
for i in range(rounds):
	factor_str = f.readline()
	factor = int(factor_str)
	count = 0

	for j in guests_list:
		if guests_list[j-1] != 0: 
			count += 1
		if count == factor:
			guests_list[j-1] = 0
			count = 0

for i in range(guests_num):
	if guests_list[i] != 0:
		print(guests_list[i])
	i += 1