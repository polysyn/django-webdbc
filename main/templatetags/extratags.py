# -*- coding: utf-8 -*-
from django import template
from django.utils.html import escape

register = template.Library()

@register.filter
def has_relation(field):
	return False

@register.filter
def get_relation(field):
	return "spell"
