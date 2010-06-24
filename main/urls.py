# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("webdbc.main.views",
	(r"^(?P<build>\d+)/(?P<tablename>\w+)/$", "tableview"),
)
