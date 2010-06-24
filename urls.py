# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("",
	(r"^static/(?P<path>.*)$", "django.views.static.serve", {"document_root": "/home/adys/src/git/webdbc/static"}),
	(r"^", include("webdbc.main.urls")),
)
