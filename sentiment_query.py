import csv


with open("reviews_60601-60606.csv") as file:
	reader = csv.reader(file)
	next(reader)
	data = [r for r in reader]

	restaurant_ids = [0]
	restaurant_sentiments = [0]
	restaurant_sums = [0]
	restaurant_counts = [0]
	restaurant_averages = [0]


	for d in data:
		try:
			rating = int(d[4])
			restaurant_id = d[9]
		except Exception as e:
			continue
			pass

		if rating >= 4:
			if restaurant_id in restaurant_ids:
				index = restaurant_ids.index(restaurant_id)
				restaurant_sentiments[index] += 1
			else:
				restaurant_ids.append(restaurant_id)
				restaurant_sentiments.append(1)
				restaurant_sums.append(rating)
				restaurant_counts.append(1)
		else:
			if restaurant_id in restaurant_ids:
				index = restaurant_ids.index(restaurant_id)
				restaurant_sentiments[index] -= 1
			else:
				restaurant_ids.append(restaurant_id)
				restaurant_sentiments.append(-1)
				restaurant_sums.append(rating)
				restaurant_counts.append(1)

			index = restaurant_ids.index(restaurant_id)
			restaurant_sums[index] += rating
			restaurant_counts[index] += 1


		#for restaurant in restaurant_ids:
		#	index1 = restaurant_ids.index(restaurant_id)
		#	restaurant_averages = restaurant_sums[index1] / restaurant_counts[index1]
		#print("test")

	print("Restarant Name, Sentiment Labels (net score), Review Rating")
	for restaurant in restaurant_ids:
		print(restaurant, end = ", ")
		print(restaurant_sentiments[restaurant_ids.index(restaurant)], end = ", \n")
		#print(restaurant_averages[restaurant_ids.index(restaurant)])

