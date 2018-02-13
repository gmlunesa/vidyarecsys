import os
import os.path
import csv
import json

# Retrieve file names in the directory
file_list = os.listdir("dataset/")

for file_name in file_list:
	# user id, rating, game id
	ratings = [file_name[:-5], 0, 0]

		# Open the file indicated by the current file name
	if file_name != ".DS_Store":
		with open("dataset/" + file_name) as src_file:

			try:
			   data = json.load(src_file)
			except json.decoder.JSONDecodeError:
				print("Invalid JSON file", file_name)

		totalgametime = 0.0

		if data is not None:
			if data["response"] is not None:
				if data["response"]["game_count"] != 0:
					if data["response"]["games"] is not None:
						# Traverse through each game owned by the user
						# Calculate total playtime 
						for item in data["response"]["games"]:
							totalgametime = totalgametime + item["playtime_forever"]

						# Get percentage
						# Save to CSV

						if totalgametime != 0:
							print ("Game time is ", totalgametime)

							for item in data["response"]["games"]:
								percentage = item["playtime_forever"] / totalgametime
								print (item["playtime_forever"], "over", totalgametime)
								print ("Percentage is ", percentage)

								if percentage >= 0.0 and percentage <= 0.20:
									ratings[1] = 1
								elif percentage >= 0.21 and percentage <= 0.40:
									ratings[1] = 2
								elif percentage >= 0.41 and percentage <= 0.60:
									ratings[1] = 3
								elif percentage >= 0.61 and percentage <= 0.80:
									ratings[1] = 4
								elif percentage >= 0.81 and percentage <= 0.100:
									ratings[1] = 5

								ratings[2] = item["appid"]

								with open('ratings.csv', 'a', newline='') as csvfile:				
									csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
									csvwriter.writerow([ratings[0],
										str(ratings[1]), 
										str(ratings[2]),
									])	
