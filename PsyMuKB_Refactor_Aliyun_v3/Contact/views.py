# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        views
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-09-24
# @update:      2018-09-24 19:02
# @Software:    PyCharm
#-------------------------------------------------------------------------------

from . import app_Contact
from flask import render_template
import json

@app_Contact.route('/')
def Contact():
	data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
			{'a': 2, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
	Json = json.dumps(data)
	# print(Json)
	return render_template('Contact.html', message=Json)