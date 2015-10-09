# -*- coding: UTF-8 -*-
#gen by plask
#a new html framework
#web service code
from flask import *
from serviceapp import app
import sys
sys.path.append('C:\Users\qianqians\Documents\workspace\DarkForce\plask\plask')
import time
import pysession

llid = []
llid.append(1)
def create_sessionid(ip):
	#获取unix时间戳
	id = str(int(time.time()))
	#用户IP
	id += '-' + ip
	#序列号
	id += '-' + str(llid[0])
	llid[0] += 1
	return id, llid[0]

def create_session(ip):
	id,sid = create_sessionid(ip)
	pysession.session[id] = {}
	pysession.session[id]["ip"] = ip
	pysession.session[id]["llid"] = sid
	pysession.session[id]["id"] = id
	print pysession.session
	js = "var sid = \"" + id + "\";"
	return js

@app.route('/vii')
@app.route('/')
def viiindex():
	css = """<!DOCTYPE html><html><head><style type="text/css">div#title1_1{width:1200px; visibility:visible; margin: 0px auto auto 220px; }div#title2_1{ visibility:visible; font-size:400%; color:rgb(252,12,12); background-color:rgb(252,252,252); margin:auto auto auto auto;}div#title2_1_1{ visibility:visible; margin:auto auto auto 0px;}div#file_c_1{width:1200px; visibility:visible; margin: 10px auto auto 220px; }div#title_input_1{width:1200px; border-style:solid; border-width: 1px; visibility:visible; margin: 10px auto auto 220px; }div#input_writer_1{ visibility:visible; float:left; margin: 5px auto auto 0px; }div#writer_edit_1{ visibility:visible; margin: 5px auto auto 0px;}div#contact_writer_1{ visibility:visible; float:left; margin: 5px auto auto 0px; }div#contact_edit_1{ visibility:visible; margin: 5px auto auto 0px;}div#title_writer_1{ visibility:visible; float:left; margin: 5px auto auto 0px; }div#title_edit_1{ visibility:visible; margin: 5px auto auto 0px;}div#text_writer_1{ visibility:visible; margin: 5px auto auto 0px;}div#text_edit_1{width:1190px; height:500px; visibility:visible; margin: 5px auto auto 2px;}div#button_1{ visibility:visible; margin: 10px auto auto 2px;}div#nbsp_1_1_1_1{ visibility:visible; margin:auto auto auto 0px;}</style></head>"""
	html = """<body><div id="title1_1"><div id="title2_1" >为祖国献礼</div></div><div id="title2_1_1" >&nbsp;</div><div id="file_c_1"></div><div id="title_input_1"><div id="input_writer_1" >作者姓名:</div><div id="writer_edit_1"><input id="writer_edit" type="text"></div><div id="contact_writer_1" >联系方式:</div><div id="contact_edit_1"><input id="contact_edit" type="text"></div><div id="title_writer_1" >标&nbsp;&nbsp;题:</div><div id="title_edit_1"><input id="title_edit" type="text"></div><div id="text_writer_1" >正&nbsp;&nbsp;文:</div><div id="text_edit_1"><textarea id="text_edit" style="height:500px;width:1190px"></textarea></div><div id="button_1"><button id="button" type="button" onclick="buttononclick(this)" >提交</button></div><div id="nbsp_1_1_1_1" >&nbsp;</div></div></body>"""
	script = """<script language="javascript" src="http://127.0.0.1:5000/JSON.js"></script><script language="javascript" src="http://127.0.0.1:5000/JSONError.js"></script><script language="javascript" src="http://127.0.0.1:5000/JSONRequestError.js"></script><script language="javascript" src="http://127.0.0.1:5000/JSONRequest.js"></script><script>function buttononclick(id){var params = {"sid":sid};
params["username"]=document.getElementById("writer_edit").value;
params["contact"]=document.getElementById("contact_edit").value;
params["title"]=document.getElementById("title_edit").value;
params["input"]=document.getElementById("text_edit").value;

JSONRequest.post("http://127.0.0.1:5000/button/submit",
params,function (requestNumber, value, exception){var board = document.getElementById("file_c_1");var dc = document.createElement("div");dc.setAttribute("id",value["title_id"]);dc.style.margin = "10px auto auto 0px";dc.style.width = "1200px";dc.style.borderStyle = "solid";dc.style.borderWidth = "1px";dc.style.clear = "both";var d = document.createElement("div");d.setAttribute("id",value["id_1"]);d.style.fontSize = "150%";var textnode=document.createTextNode(value["title"]);d.appendChild(textnode);var dt = document.createElement("div");dt.setAttribute("id",value["id_1_1"]);var textnode=document.createTextNode(value["input"]);dt.appendChild(textnode);var dz = document.createElement("div");dz.style.fontSize = "50%";dz.style.cssFloat="left";dz.style.margin = "10px auto 5px auto";var textnode=document.createTextNode("作者:");dz.appendChild(textnode);var dzu = document.createElement("div");dzu.style.cssFloat="left";dzu.style.fontSize = "50%";dzu.style.margin = "10px 5px 5px auto";var textnode=document.createTextNode(value["username"]);dzu.appendChild(textnode);var dl = document.createElement("div");var textnode=document.createTextNode("联系方式:");dl.style.cssFloat="left";dl.style.fontSize = "50%";dl.style.margin = "10px auto 5px auto";dl.appendChild(textnode);var dlc = document.createElement("div");var textnode=document.createTextNode(value["contact"]);dlc.appendChild(textnode);dlc.style.fontSize = "50%";dlc.style.margin = "10px auto 5px auto";dc.appendChild(d);dc.appendChild(dt);dc.appendChild(dz);dc.appendChild(dzu);dc.appendChild(dl);dc.appendChild(dlc);if (board.firstChild){board.insertBefore(dc, board.firstChild);}else{board.appendChild(dc);}});}
""" + create_session(request.remote_addr)
	return css + html + script + "</script></html>"

@app.route('/button/submit',methods=['POST'])
def buttonsubmit():
	import traceback
	from appglobal import cb_mothed
	from io import BytesIO
	import json
	r = {}
	try:
		for cb in cb_mothed["button"]["submit"]:
			r.update(cb(request.get_json()))
		return Response(BytesIO(json.dumps(r)), mimetype='text/json')
	except:
		from log import log
		log(traceback.format_exc())

@app.route('/JSON.js')
def file_JSON():
	from io import BytesIO
	from appglobal import res_data
	import traceback
	try:
		return Response(BytesIO(res_data['JSON.js']), mimetype='js')
	except:
		from log import log
		log(traceback.format_exc())

@app.route('/JSONError.js')
def file_JSONError():
	from io import BytesIO
	from appglobal import res_data
	import traceback
	try:
		return Response(BytesIO(res_data['JSONError.js']), mimetype='js')
	except:
		from log import log
		log(traceback.format_exc())

@app.route('/JSONRequest.js')
def file_JSONRequest():
	from io import BytesIO
	from appglobal import res_data
	import traceback
	try:
		return Response(BytesIO(res_data['JSONRequest.js']), mimetype='js')
	except:
		from log import log
		log(traceback.format_exc())

@app.route('/JSONRequestError.js')
def file_JSONRequestError():
	from io import BytesIO
	from appglobal import res_data
	import traceback
	try:
		return Response(BytesIO(res_data['JSONRequestError.js']), mimetype='js')
	except:
		from log import log
		log(traceback.format_exc())

