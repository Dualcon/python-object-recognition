#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import platform


def say(string):
	platform.system()
	platform.release()
	if(os.name == "posix"):
		os.system("say " + string)
