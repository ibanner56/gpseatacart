#!flask/bin/python
from flask import *

app = Flask(__name__)
datastore = {}

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

@app.route('/query', methods=['POST'])
def query_datastore():
	if not request.json or not 'cards' in request.json:
		abort(400)
	results = {}
	results["cards"] = []
	
	for card in request.json["cards"]:
		if card in datastore:
			results["cards"].append(datastore[card])

	return jsonify(results), 200

if __name__ == '__main__':
	init()
	app.run(debug=True, host='0.0.0.0')
