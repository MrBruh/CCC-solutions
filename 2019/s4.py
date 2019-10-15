def largest_shift(largest_list, largest_number, index):
	print(largest_list, largest_number)
	list_range = len(largest_list)
	for i in range(list_range):
		if i == list_range - 1:
			largest_list[0] = [largest_number, index]
			return largest_list

		if largest_list[list_range - i - 2][0] != 0:
			largest_list[list_range - i - 1] = largest_list[list_range - i - 2]
		else:
			pass
	return largest_list

def check_in_range(indexes, max_days, remainder):
	indexes.sort()
	#print(indexes)
	if indexes[0] >= max_days:
		#print("too far from start")
		return False

	current_day = 0
	for day in range(len(indexes) - 1):
		current_day += (day + 1) * max_days

		if current_day >= indexes[day] and current_day < indexes[day + 1]:
			continue
		else:
			i = 0
			for i in range(remainder):
				current_day -= 1
				#print(current_day, indexes[day], indexes[day + 1])
				if current_day >= indexes[day] and current_day < indexes[day + 1]:
					break
				if i == remainder-1:
					#print("used too many days", )
					return False
			remainder -= i

	return True

def recursive_test(attractions_list, remplacement_list, max_days, remainder):
	remplacement_list_len = len(remplacement_list)
	if remplacement_list_len == 1:
		test_list = []
		for i in attractions_list:
			for j in attractions_list:
				if j[1] == i[1]:
					test_list.append(remplacement_list[1])
				else:
					test_list.append(j[1])
			if check_in_range(test_list, max_days, remainder) == True:
				max_sum = 0
				for j in attractions_list:
					if j[1] == i[1]:
						max_sum += remplacement_list[0]
					else:
						max_sum += j[0]
				return max_sum
		#0 = none of the given combinations worked
		return 0
	else:
		test_list = []
		output = 0
		for i in attractions_list:
			for j in attractions_list:
				if j[1] == i[1]:
					test_list.append(remplacement_list[0:remplacement_list_len-1])
				else:
					test_list.append(j[1])
			output = recursive_test(test_list, remplacement_list[0:remplacement_list_len-2], max_days, remainder)
			if output != 0:
				return output


def main(): 
	f = open("s4.1-06.in", "r")
	information_string = f.readline()
	information = information_string.split()

	attractions = int(information[0])
	max_days = int(information[1])

	numbers_string = f.readline()
	numbers = numbers_string.split()

	day_range = 0
	if(attractions % max_days == 0):
		day_range = attractions / max_days
		largest_in_window = 0
		total_points = 0

		for i in range(day_range):
			for number in numbers[(max_days*i):(max_days*i) + max_days]:
				if int(number) > largest_in_window:
					largest_in_window = int(number)

			total_points += int(largest_in_window)
			largest_in_window = 0

		print(total_points)
		return 0
	else:
		day_range = 1 + int(attractions / max_days)

	largest_attractions = []
	attraction_template = [0, 0]
	for i in range(day_range):
		largest_attractions.append(attraction_template)

	#print(largest_attractions, day_range)
	attraction_index = 0
	shift_index = 0
	for i in numbers:
		for j in largest_attractions:
			print(shift_index, len(largest_attractions), largest_attractions)
			if i >= j[0]:
				largest_attractions = largest_shift(largest_attractions[shift_index:len(largest_attractions)], i, attraction_index)
			shift_index += 1

		attraction_index += 1

	print(largest_attractions)

	index_list = []
	for i in largest_attractions:
		index_list.append(i[1])

	max_points = 0
	if check_in_range(index_list, max_days, max_days - (attractions % max_days)) == True:
		for i in largest_attractions:
			max_points += int(i[0])
		print(max_points)
		return 0
	else:
		print("unimplemented")
		return 1

if __name__ == "__main__":
	main()