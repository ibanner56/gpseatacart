#!flask/bin/python
from flask import *

app = Flask(__name__)
datastore = {}
secondary_lkup = {}

def init():
	artcards = open("data/GPSTART.csv")

	# Parse the cards database
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
		index = artist + "/" + name		

		if(index in datastore):
			datastore[index]["printings"].append(printing)
		else:
			datastore[index] = {"name": name, "artist": artist, "printings": [printing], "multiverseid": multiverseid}
			name = name.lower()
			if(name in secondary_lkup):
				secondary_lkup[name].append(index)
			else:
				secondary_lkup[name] = [index]

@app.route('/', methods=['OPTIONS'])
def query_options():
	response = Response()
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
	return response

@app.route('/', methods=['POST'])
def query_datastore():
	if not request.json or not 'cards' in request.json:
		abort(400)
	results = {}
	results["cards"] = []
	
	for card in request.json["cards"]:
		card = card.lower()
		if card in secondary_lkup:
			for index in secondary_lkup[card]:
				results["cards"].append(datastore[index])
	
	response = jsonify(results)
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

	return response, 200

if __name__ == '__main__':
	init()
	app.run(host='0.0.0.0')
