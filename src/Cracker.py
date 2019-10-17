# IdentifyHacker.py

# Josue Lopez

""" This module is intended to receive a file name and parse through a log of HTTP request, 
in order to idenitify if a hacker attempted to use an SQL injection to hack a database.
"""

from collections import defaultdict
from httpResponse import httpResponse as httpResponse

class Cracker():
	def __init__(self, URL:str):
		self.fileName = sys_fileName
		self.linesOfFile = []
		self.map = defaultdict(list)


