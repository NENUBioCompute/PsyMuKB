# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        __init__.py
# @Author:      GuoSijia
# @Purpose:     Browser
# @Created:     2018-09-24
# @update:      2018-09-24 17:07
# @Software:    PyCharm
#-------------------------------------------------------------------------------
from flask import Blueprint


app_Browser = Blueprint("browser", __name__, template_folder="templates")

# import views
from Browse import views