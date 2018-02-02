
import json
import os
import os.path
import requests
import time

# Convert to JSON object
file_name = 'applist.json'

with open(file_name, encoding="utf8") as src_file:
    data = json.load(src_file)

# Traverse through all ID's in the JSON object
# For each ID in the JSON object
for item in data["applist"]["apps"]:
	# Query the app details from the Steam store
	current_appid = item["appid"]
	url = 'http://store.steampowered.com/api/appdetails?appids=' + str(item["appid"]) + '&format=json'

	# Retrieve the response
	r = requests.get(url = url).json()
	time.sleep(2)

	# Tracing
	print(r)
	print("ID: ", str(current_appid))

	if r is not None:

		if str(current_appid) in r is not None:
			if "success" in r[str(current_appid)] is not None:
				if r[str(current_appid)]["success"]:
					print("Success: ", r[str(current_appid)]["success"])
					is_genre = "genres" in r[str(current_appid)]["data"]

					if is_genre:

						# Get the "genre" element from the response 
						genres = r[str(current_appid)]["data"]["genres"]

						# Insert a new element called genre in the entry in the JSON object
						item["genres"] = genres
				else:
					print(str(current_appid))
					item["genres"] = []
			else:
				print("Success is a NoneType")
				item["genres"] = []
		else:
			print("current_appid is a NoneType")
			item["genres"] = []
	else:
		print("r is a NoneType")
		item["genres"] = []


# Save as new JSON object
with open('applist_genre.json','w') as f:
    json.dump(data, f)



