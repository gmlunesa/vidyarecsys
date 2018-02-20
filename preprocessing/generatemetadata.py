import os
import os.path
import csv
import json
import requests
import time

with open("applist_genre.json", encoding="utf8") as applist:
	applist_data = json.load(applist)

for item in applist_data:
	game_data = [item, "", ""]

	url = 'http://store.steampowered.com/api/appdetails?appids=' + item + '&format=json'

	# Retrieve the response
	r = requests.get(url = url).json()
	time.sleep(2)

	if r is not None:

		if str(item) in r is not None:
			if "success" in r[str(item)] is not None:
				if r[str(item)]["success"]:
					print("Success: ", r[str(item)]["success"])
					is_genre = "genres" in r[str(item)]["data"]

					if is_genre:
						print("Successfully queried", str(item))
						
						game_data[1] = r[str(item)]["data"]["name"]

						genres = r[str(item)]["data"]["genres"]

						for genre in genres:
							game_data[2] = game_data[2] + str(genre["id"]) + "/"
						
						with open('metadata.csv', 'a', newline='') as csvfile:				
							csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
							csvwriter.writerow([game_data[0],
								str(game_data[1]), 
								str(game_data[2]),
							])	
							
				else:
					print(str(item))
			else:
				print("Success is a NoneType")
		else:
			print("current_appid is a NoneType")
	else:
		print("r is a NoneType")