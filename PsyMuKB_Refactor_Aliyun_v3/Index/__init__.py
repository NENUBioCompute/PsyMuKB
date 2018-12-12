# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        __init__.py
# @Author:      GuoSijia
# @Purpose:     Index首页模块
# @Created:     2018-09-23
# @update:      2018-09-23 23:58
# @Software:    PyCharm
#-------------------------------------------------------------------------------

from flask import Blueprint


app_Index = Blueprint("index", __name__, template_folder="templates")

# import views
from Index import views