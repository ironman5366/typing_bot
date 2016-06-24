import time
import sys
from splinter.browser import Browser
browser = Browser('chrome')
browser.visit('http://typing-speed-test.aoeu.eu/')
input_field = browser.find_by_id("input")
while True:
	try:
		current_word = browser.find_by_id("currentword")
		input_field.type("{0} ".format(current_word.value))
	except AttributeError:
		print "Done"
		sys.exit()