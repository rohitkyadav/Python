import csv

rows = [['1', '2', '3'], ['4', '5', '6']]

with open('my.csv', 'w+', newline='') as csv_file:
	writer = csv.writer(csv_file)
	for row in rows:
		writer.writerow(row)

with open('my.csv', 'r+', newline='') as csv_file:
	reader = csv.reader(csv_file)
	for row in reader:
		print(str(row))