# -*- coding: UTF-8 -*-
#gen by plask
#a new html framework
#web service code
from flask import *
import pymongo

conn = pymongo.Connection('localhost',27017)
db = conn.vii
collection = db.viitext

app = Flask(__name__)

@app.route('/vii')
@app.route('/')
def viiindex():
	import os
	file = open("./vii.html")
	return file.read()

@app.route('/button/submit',methods=['POST'])
def buttonsubmit():
	import traceback
	from io import BytesIO
	import json
	try:
		p = request.get_json()
		r = {}
		r.update(p)
		collection.insert(r)
		text = p["input"]
		if len(text) > 100:
			p["input"] = text[:100] + "..."
		title = p["title"]
		p["title_id"] = "title_" + title
		p["id_1"] = title + "_1"
		p["id_1_1"] = title + "_1_1"
		p["id_1_1_1"] = title + "_1_1_1"
		return Response(BytesIO(json.dumps(p)), mimetype='text/json')
	except:
		print(traceback.format_exc())

@app.route('/JSON.js')
def file_JSON():
	from io import BytesIO
	import traceback
	try:
		filejson = open('JSON.javascript', 'rb')
		json = filejson.read()
		return Response(BytesIO(json), mimetype='js')
	except:
		print(traceback.format_exc())

@app.route('/JSONError.js')
def file_JSONError():
	from io import BytesIO
	import traceback
	try:
		filejson = open('JSONError.javascript', 'rb')
		json = filejson.read()
		return Response(BytesIO(json), mimetype='js')
	except:
		print(traceback.format_exc())

@app.route('/JSONRequest.js')
def file_JSONRequest():
	from io import BytesIO
	import traceback
	try:
		filejson = open('JSONRequest.javascript', 'rb')
		json = filejson.read()
		return Response(BytesIO(json), mimetype='js')
	except:
		print(traceback.format_exc())

@app.route('/JSONRequestError.js')
def file_JSONRequestError():
	from io import BytesIO
	import traceback
	try:
		filejson = open('JSONRequestError.javascript', 'rb')
		json = filejson.read()
		return Response(BytesIO(json), mimetype='js')
	except:
		print(traceback.format_exc())

def main():
	app.run("127.0.0.1", 5000, threaded = True)

if __name__ == '__main__':
	main()

