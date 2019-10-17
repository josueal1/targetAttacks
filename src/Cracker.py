# IdentifyHacker.py

# Josue Lopez

""" This module is intended to receive a file name and parse through a log of HTTP request, 
in order to idenitify if a hacker attempted to use an SQL injection to hack a database.
"""

from collections import defaultdict
from src.httpResponse import httpResponse as httpResponse

class Cracker():
	
    def __init__(self, sys_fileName:str):
		self.fileName = sys_fileName
		self.linesOfFile = []
		self.map = defaultdict(list)
    
    def collectLinesOfFile(self):
        try: 
            file1 = open(self.fileName, "r")
            self.linesOfFile = file1.readlines()
        except Exception as e:
            print("Collection Error: ", str(e))
            raise e
    
    def storeLinesThatContains(self, token:str):
        for line in self.linesOfFile:
            if token in line:
                self.map[token].append(line)

	@staticmethod
	def printNFileLines(linesOfFile, n: int):
		if n > len(linesOfFile):
			print("Error:  Nth amount larger than # of lines")
			raise IndexError

		for i in range(n):
			try:
				print(linesOfFile[i])
			except Exception as e:
				print("Print Error: ", str(e),"possibly index issue")
				raise e

	
