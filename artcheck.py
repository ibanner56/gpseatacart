import json

def main():
	artcards = open("GPSTART.csv")
	cards = open("cards.txt")
	datastore = {}
	result = {}	

	for line in artcards:
		data = line.split(",")
		if(len(data) > 7):
			# The name had a comma in it...
			name = data[1] + "," + data[2]
			multiverseid = data[3].split("=")[1]
		else:
			name = data[1]
			multiverseid = data[2].split("=")[1]
		artist = data[3]
		printing = data[6].strip()
		index = name.lower()
		if(index in datastore):
			datastore[index]["printings"].append(printing)
		else:
			datastore[index] = {"artist": artist, "printings": [printing], "multiverseid": multiverseid}
	
	for line in cards:
		line = line.strip()
		if(line.lower() in datastore):
			result[line] = datastore[line.lower()]
	print(json.dumps(result))
main()
