#!/usr/bin/python3
# -*- coding: utf-8 -*-

import importlib.machinery


def load(identifier, path):
	""" Loads a py file.

	Args:
	identifier: a string to identify the py file.
	path: a string with the path to the py file.

	Returns:
	handle: A handle to the file.
	"""
	loader = importlib.machinery.SourceFileLoader(identifier, path)
	handle = loader.load_module(identifier)
	return handle
