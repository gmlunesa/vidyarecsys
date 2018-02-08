import os
import os.path
import csv
import json

# Retrieve file names in the directory
file_list = os.listdir("dataset/")

with open("applist_genre.json", encoding="utf8") as applist:
  applist_data = json.load(applist)

# Loop through each json file in the directory
for file_name in file_list:

	# Action 				[1] 1
	# Strategy 				[2] 2
	# RPG					[3] 3
	# Indie 				[4] 23
	# Adventure 			[5] 25
	# Sports				[6] 18
	# Simulation			[7] 28
	# MMO		 			[8] 29
	# Free 			 		[9] 37
	# Casual 				[10] 4

	# Make an array of corresponding features
	genre_features = [file_name[:-5], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	# Open the file indicated by the current file name
	if file_name != ".DS_Store":
		with open("dataset/" + file_name) as src_file:
		    data = json.load(src_file)

		if data is not None:
			if data["response"] is not None:
				if data["response"]["games"] is not None:
					# Traverse through each game owned by the user
					for item in data["response"]["games"]:

						print(item["appid"])

						# if genre list contains the game item
						if applist_data[str(item["appid"])] is not None:

							# Loop through the genres of the said item
							for genres in applist_data[str(item["appid"])]:

								if genres["id"] is not None:
									if genres["id"] == '1':
										genre_features[1] = genre_features[1] + 1
									elif genres["id"] == '2':
										genre_features[2] = genre_features[2] + 1
									elif genres["id"] == '3':
										genre_features[3] = genre_features[3] + 1
									elif genres["id"] == '23':
										genre_features[4] = genre_features[4] + 1
									elif genres["id"] == '25':
										genre_features[5] = genre_features[5] + 1
									elif genres["id"] == '18':
										genre_features[6] = genre_features[6] + 1
									elif genres["id"] == '28':
										genre_features[7] = genre_features[7] + 1
									elif genres["id"] == '29':
										genre_features[8] = genre_features[8] + 1
									elif genres["id"] == '37':
										genre_features[9] = genre_features[9] + 1
									elif genres["id"] == '4':
										genre_features[10] = genre_features[10] + 1

									print(genre_features)

						
		

		# Print to CSV file tbh	
		with open('matrixdata.csv', 'a', newline='') as csvfile:				
			csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
			csvwriter.writerow([genre_features[0], str(genre_features[1]), 
				str(genre_features[2]),
				str(genre_features[3]),
				str(genre_features[4]),
				str(genre_features[5]),
				str(genre_features[6]),
				str(genre_features[7]),
				str(genre_features[8]),
				str(genre_features[9]),
				str(genre_features[10])])	
