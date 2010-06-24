# -*- coding: utf-8 -*-

import os.path
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from pywow.wdbc.environment import Environment


ENVIRONMENTS = {}

def get_environment(build):
	build = int(build)
	if build not in ENVIRONMENTS:
		try:
			ENVIRONMENTS[build] = Environment(build)
		except ValueError:
			raise Http404
	
	return ENVIRONMENTS[build]


def tableview(request, build, tablename):
	env = get_environment(build)
	if tablename not in env:
		raise Http404
	table = env[tablename]
	return render_to_response("tableview.html", {"build": build, "table": table, "tablename": os.path.basename(table.file.name)})

def buildview(request, build):
	return render_to_response("buildview.html", {"build": build, "environment": get_environment(build)})
