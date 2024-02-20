#!/usr/bin/env python3
import csv
filename = "souteze.csv"

monthCol = 0
nameCol = 1
teamCol = 2
urlCol = 3
notesCol = 4

with open(filename, newline='') as csvFile:
	dataObject = csv.reader(csvFile, delimiter=',', quotechar='"')

	print("|Měsíc|Tým|Jméno|Poznámky|")
	print("|---|---|---|---|")

	for row in dataObject: # |month|team|[name](url) (notes)|
		if dataObject.line_num == 1:
			continue
		print("|" + row[monthCol] + "|" + row[teamCol] + "|[" + row[nameCol] + "](" + row[urlCol] + ")|" + row[notesCol] + "|")