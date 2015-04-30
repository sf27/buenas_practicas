# -*- coding: utf-8 -*-

def k(**kwargs):
	print("kwargs: ", type(kwargs), dict(kwargs), kwargs)
	return kwargs

def a(*args):
	print("args: ", type(args), args[0], args)
	return args


a(range(3), range(2))
k(a=5)