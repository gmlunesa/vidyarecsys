import os
import os.path
import csv
import json
import pandas


def label(directory):

	colnames = ['appid']
	applist_df = pandas.read_csv('metadata.csv', delimiter=',')

	applist_arr = applist_df['appid'].tolist()

	with open("applist_genre_original.json", encoding="utf8") as applist:
	  applist_data = json.load(applist)

	# Retrieve file names in the directory
	file_list = os.listdir(directory)

	ctr = 0
	overall_ctr = 0

	for file_name in file_list:
		# user id, rating, game id
		ratings = [file_name[:-5], 0, 0]

		

		# Open the file indicated by the current file name
		if file_name != ".DS_Store":
			overall_ctr = overall_ctr + 1
			print (overall_ctr, "/", len(file_list),"users processed: ", file_name)	
			with open(directory + file_name) as src_file:

				try:
					data = json.load(src_file)
					totalgametime = 0.0
					lowest_playtime = 0.0
					highest_playtime = 0.0
					percentage = 0.0

					if data is not None:
						if data["response"] is not None:
							if data["response"]["game_count"] != 0:
								if data["response"]["games"] is not None:
									# Traverse dataset and find the lowest and highest play time values
									i = 0

									for item in data["response"]["games"]:
										if item["playtime_forever"] != 0 and str(item["appid"]) in applist_data:

											# Calculate total playtime 
											totalgametime = totalgametime + item["playtime_forever"]
											if i == 0:
												lowest_playtime = item["playtime_forever"]
												highest_playtime = item["playtime_forever"]
											else:
												if item["playtime_forever"] < lowest_playtime:
													lowest_playtime = item["playtime_forever"]
												elif item["playtime_forever"] > highest_playtime:
													highest_playtime = item["playtime_forever"]

											i =  i + 1

									# Calculate space between playtimes
									# if highest_playtime == lowest_playtime:
									# 	space = highest_playtime
									# else:
									# 	space = highest_playtime - lowest_playtime

									space = highest_playtime

									# Get percentage
									# Save to CSV
										# print ("Game time is ", totalgametime)

									for item in data["response"]["games"]:
										game_ctr = 0
										# check if appid is in the valid app ids list
										if int(item["appid"]) in applist_arr and space != 0:
											percentage = item["playtime_forever"] / space
											# print (item["playtime_forever"], "over", space)
											# print ("Percentage is ", percentage)

											decimal = round(percentage, 2) * 100
											decimal = (decimal * 5) % 100
											decimal = decimal * 0.01
											decimal = round(decimal, 2)

											if percentage >= 0.0 and percentage <= 0.20:
												ratings[1] = 1 + decimal
											elif percentage > 0.20 and percentage <= 0.40:
												ratings[1] = 2 + decimal
											elif percentage > 0.40 and percentage <= 0.60:
												ratings[1] = 3 + decimal
											elif percentage > 0.60 and percentage <= 0.80:
												ratings[1] = 4 + decimal
											elif percentage > 0.80:
												ratings[1] = 5 + decimal

											ratings[2] = item["appid"]

											with open('ratings.csv', 'a', newline='') as csvfile:				
												csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
												csvwriter.writerow([ratings[0], str(ratings[1]), str(ratings[2])])

											game_ctr = game_ctr + 1
											print (game_ctr , " / ", data["response"]["game_count"])

										elif int(item["appid"]) in applist_arr and space == 0:

											percentage = item["playtime_forever"]
											if percentage >= 0.0:
												ratings[1] = 1

											ratings[2] = item["appid"]

											with open('ratings.csv', 'a', newline='') as csvfile:				
												csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
												csvwriter.writerow([ratings[0], str(ratings[1]), str(ratings[2])])

											game_ctr = game_ctr + 1
											print (game_ctr , " / ", data["response"]["game_count"])


										else:
											
											print(str(item["appid"]) in applist_data, " : ", item["appid"], "is not on the applist")

									ctr = ctr + 1			
									print (ctr, "/", len(file_list),"users added: ", file_name)
								else:
									print("b")
							else:
								print("c")
						else:
							print("d")

					else: 
						print("e")

				except json.decoder.JSONDecodeError:
					print("Invalid JSON file", file_name)

label('dataset/')
