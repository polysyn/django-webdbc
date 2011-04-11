# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns("",
	url(r"^static/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
	url(r"^", include("webdbc.main.urls")),
)
