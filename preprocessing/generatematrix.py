import os
import os.path
import csv
import json

# Retrieve file names in the directory
file_list = os.listdir("data/")

with open("applist_genre.json", encoding="utf8") as applist:
  applist_data = json.load(applist)

# Loop through each json file in the directory
for file_name in file_list:

	# Action 				[0]
	# Strategy 				[1]
	# RPG					[2]
	# Indie 				[3]
	# Adventure 			[4]
	# Sports				[5]
	# Simulation			[6]
	# Early Access 			[7]
	# Ex Early Access 		[8]
	# MMO 					[9]
	# Free 					[10]

	# Make an array of corresponding features
	genre_features = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	# Open the file indicated by the current file name
	with open("data/" + file_name, encoding="utf8") as src_file:
	    data = json.load(src_file)

	if data is not None:
		if data["response"] is not None:
			# Traverse through each game
			for item in data["response"]["games"]:
				for genre in applist_data[str(item["appid"])]["genres"]:

					# To Do: Investigate what indices do the genres have via steam spy https://steamdb.info/genres/
					print(genre["id"])

					genre_features[0] = genre_features[0] + 1

					print(genre_features)

					



# loop through each json file in the directory
	# loop through go on ["response"]["games"]
		# access ["response"]["games"] genre id and then cross reference it to the general app list
		# increment the genre category of that person
		#
		#

# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam', 'Baked Beans'])
# #     spamwriter.writerow(['Spam',
#  'Lovely Spam', 'Wonderful Spam'])
