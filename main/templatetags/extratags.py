# -*- coding: utf-8 -*-
from django import template
from django.utils.html import escape
from pywow.wdbc.structures.fields import ForeignKeyBase

register = template.Library()

@register.filter
def zip(value, arg):
	_zip = __builtins__["zip"] # XXX: WTF django? Dict instead of module?
	return _zip(value, arg)

@register.filter
def sort(arg):
	return sorted(arg)

@register.filter
def has_relation(field):
	return isinstance(field, ForeignKeyBase)

@register.filter
def get_relation(field, value):
	return field.get_relation(value)
