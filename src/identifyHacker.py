"""The identifyHacker.py module utilizes the Cracker API as client code to find any
 hacking HTTP responses from a local file."""

from src.Cracker import Cracker as Cracker

if __name__ == "__main__":
	t = Cracker("hacked.txt")
	t.collectLinesOfFile()
	for i in ["target", "404", "DELETE"]:
		t.storeLinesThatContains(str(i))

	# Cracker.printNFileLines(t.map["404"], 46)

	NotFounds = t.map["404"]
	deleteRequests = t.map["DELETE"]
	targetAttacks = t.map["target"]

	for line in targetAttacks:
		print(line)
