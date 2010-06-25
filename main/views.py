# -*- coding: utf-8 -*-

import os.path
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from pywow.wdbc.environment import Environment


ENVIRONMENTS = {}
ITEMS_PER_PAGE = 100

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
	
	page = request.GET.get("p", 1)
	try:
		page = int(page)
	except ValueError:
		page = 1
	
	data = table[:]
	start = ITEMS_PER_PAGE * (page-1)
	stop = start + ITEMS_PER_PAGE
	count = len(table)
	if count > ITEMS_PER_PAGE * 1.5:
		data = table[start:stop]
	
	return render_to_response("tableview.html", {
		"build": build,
		"table": table,
		"tablename": os.path.basename(table.file.name),
		"page": page,
		"page_max": count / ITEMS_PER_PAGE + 1,
		"data": data,
		"min": start + 1,
		"max": min(count, stop),
	})


def buildview(request, build):
	return render_to_response("buildview.html", {"build": build, "environment": get_environment(build)})
