# -*- coding: UTF-8 -*-
# vii
# create at 2015/9/1
# autor: qianqians

import sys
import pymongo
sys.path.append('../')
from plask import *

collection = None

def create_title(id, cname, name, praframe):
	c = pycontainer('title_' + id, pyhtmlstyle.margin_auto, praframe)
	c.set_location(0, 10)
	c.set_size(1200, 0)
	c.set_border_style(pyhtmlstyle.solid)
	c.set_border_size(1)

	title = pytext(cname, id, pyhtmlstyle.margin_left, c)
	title.set_font_size(150)
	ev = uievent('http://127.0.0.1:5000/', title, pyelement.onmouseover)
	ev.add_call_ui(title.client_set_text_decoration(pyhtmlstyle.UnderlineDecoration))
	ev.add_call_ui(title.client_set_cursor(pyhtmlstyle.pointer))
	title.register_uievent(ev)
	evo = uievent('http://127.0.0.1:5000/', title, pyelement.onmouseout)
	evo.add_call_ui(title.client_set_text_decoration(pyhtmlstyle.NoneDecoration))
	evo.add_call_ui(title.client_set_cursor(pyhtmlstyle.auto))
	title.register_uievent(evo)

	title = pytext(name, id + "_1_1", pyhtmlstyle.margin_left, c)
	title.set_location(0, 10)

	title = pytext("&nbsp;", id + "_1_1_1", pyhtmlstyle.margin_left, c)

def add_title():
	code = "var board = document.getElementById(\"file_c_1\");"
	code += "var dc = document.createElement(\"div\");"
	code += "dc.setAttribute(\"id\",value[\"title_id\"]);"
	code += "dc.style.margin = \"10px auto auto 0px\";"
	code += "dc.style.width = \"1200px\";"
	code += "dc.style.borderStyle = \"solid\";"
	code += "dc.style.borderWidth = \"1px\";"
	code += "dc.style.clear = \"both\";"
	code += "var d = document.createElement(\"div\");"
	code += "d.setAttribute(\"id\",value[\"id_1\"]);"
	code += "d.style.fontSize = \"150%\";"
	code += "var textnode=document.createTextNode(value[\"title\"]);"
	code += "d.appendChild(textnode);"
	code += "var dt = document.createElement(\"div\");"
	code += "dt.setAttribute(\"id\",value[\"id_1_1\"]);"
	code += "var textnode=document.createTextNode(value[\"input\"]);"
	code += "dt.appendChild(textnode);"
	code += "var dz = document.createElement(\"div\");"
	code += "dz.style.fontSize = \"50%\";"
	code += "dz.style.cssFloat=\"left\";"
	code += "dz.style.margin = \"10px auto 5px auto\";"
	code += "var textnode=document.createTextNode(\"作者:\");"
	code += "dz.appendChild(textnode);"
	code += "var dzu = document.createElement(\"div\");"
	code += "dzu.style.cssFloat=\"left\";"
	code += "dzu.style.fontSize = \"50%\";"
	code += "dzu.style.margin = \"10px 5px 5px auto\";"
	code += "var textnode=document.createTextNode(value[\"username\"]);"
	code += "dzu.appendChild(textnode);"
	code += "var dl = document.createElement(\"div\");"
	code += "var textnode=document.createTextNode(\"联系方式:\");"
	code += "dl.style.cssFloat=\"left\";"
	code += "dl.style.fontSize = \"50%\";"
	code += "dl.style.margin = \"10px auto 5px auto\";"
	code += "dl.appendChild(textnode);"
	code += "var dlc = document.createElement(\"div\");"
	code += "var textnode=document.createTextNode(value[\"contact\"]);"
	code += "dlc.appendChild(textnode);"
	code += "dlc.style.fontSize = \"50%\";"
	code += "dlc.style.margin = \"10px auto 5px auto\";"
	code += "dc.appendChild(d);"
	code += "dc.appendChild(dt);"
	code += "dc.appendChild(dz);"
	code += "dc.appendChild(dzu);"
	code += "dc.appendChild(dl);"
	code += "dc.appendChild(dlc);"
	code += "if (board.firstChild){board.insertBefore(dc, board.firstChild);}else{board.appendChild(dc);}"
	return code

def create_input(praframe):
	c = pycontainer('title_input', pyhtmlstyle.margin_auto, praframe)
	c.set_location(220, 10)
	c.set_size(1200, 0)
	c.set_border_style(pyhtmlstyle.solid)
	c.set_border_size(1)

	title = pytext("作者姓名:", "input_writer", pyhtmlstyle.float_left, c)
	title.set_location(0, 5)
	titleusername = pyedit('writer_edit', pyedit.text, pyhtmlstyle.margin_left, c)
	titleusername.set_location(0, 5)
	title = pytext("联系方式:", "contact_writer", pyhtmlstyle.float_left, c)
	title.set_location(0, 5)
	titlecontact = pyedit('contact_edit', pyedit.text, pyhtmlstyle.margin_left, c)
	titlecontact.set_location(0, 5)
	title = pytext('标&nbsp;&nbsp;题:', "title_writer", pyhtmlstyle.float_left, c)
	title.set_location(0, 5)
	titletitle = pyedit('title_edit', pyedit.text, pyhtmlstyle.margin_left, c)
	titletitle.set_location(0, 5)
	title = pytext('正&nbsp;&nbsp;文:', "text_writer", pyhtmlstyle.margin_left, c)
	title.set_location(0, 5)
	titletext = pyedit('text_edit', pyedit.textarea, pyhtmlstyle.margin_left, c)
	titletext.set_location(2, 5)
	titletext.set_size(1190, 500)

	button = pybutton('提交', 'button', pyhtmlstyle.margin_left, c)
	ev = uievent('http://127.0.0.1:5000/', button, pyelement.onclick)
	params = jparams()
	params.append("username", titleusername.client_get_input_text())
	params.append("contact", titlecontact.client_get_input_text())
	params.append("title", titletitle.client_get_input_text())
	params.append("input", titletext.client_get_input_text())
	onsev = on_server_response()
	sev = server_event("submit", params, onsev)
	def on_click(p):
		#collection.insert(p)
		text = p["input"]
		if len(text) > 100:
			p["input"] = text[:100] + "..."
		title = p["title"]
		p["title_id"] = "title_" + title
		p["id_1"] = title + "_1"
		p["id_1_1"] = title + "_1_1"
		p["id_1_1_1"] = title + "_1_1_1"
		return p
	sev.add_onevent(on_click)
	onsev.add_call(add_title())
	ev.add_server_event(sev)
	button.register_uievent(ev)
	button.set_location(2, 10)

	title = pytext("&nbsp;", "nbsp_1_1_1", pyhtmlstyle.margin_left, c)

def layout():
	conn = pymongo.Connection('localhost',27017)
	db = conn.vii
	collection = db.viitext

	app = plaskapp('0.0.0.0', 5000)

	p = pypage('vii', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_auto)
	p.add_page_route('/')

	b = pycontainer('title1', pyhtmlstyle.margin_auto, p)
	b.set_location(220, 0)
	b.set_size(1200, 0)

	title = pytext("为祖国献礼", "title2", pyhtmlstyle.margin_auto, b)
	title.set_background_color((252,252,252))
	title.set_font_color((252,12,12))
	title.set_font_size(400)

	title = pytext("&nbsp;", "title2" + "_1", pyhtmlstyle.margin_left, p)

	c = pycontainer('file_c', pyhtmlstyle.margin_auto, p)
	c.set_location(220, 10)
	c.set_size(1200, 0)

	create_input(p)

	p.init()

	app.run()

if __name__ == '__main__':
	layout()
