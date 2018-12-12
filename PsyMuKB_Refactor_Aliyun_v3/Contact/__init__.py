# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        __init__.py
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-09-24
# @update:      2018-09-24 17:08
# @Software:    PyCharm
#-------------------------------------------------------------------------------

from flask import Blueprint


app_Contact = Blueprint("contact", __name__, template_folder="templates")

# import views
from Contact import views