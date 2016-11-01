#9fb8cd70cb34cab8e83690473133f51943b5c93f

import os
import csv
import random
import string

#cur_dirpath = os.getcwd()
#filename = "choices.csv"
#file_path = os.path.join(os.getcwd(), filename) 

def get_file_path(filename):
	cur_dirpath = os.getcwd()
	file_path = os.path.join(os.getcwd(), filename) 
	print(file_path)
	return file_path

path = get_file_path("goog.csv")

def get_random_string():
	rnstring = ""
	for i in range(0, 4):
		rnstring += random.choice(string.ascii_letters)
	return rnstring 


def read_csv(filepath):
	with open (filepath, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			#try:
		 		print(row)#[0], row[1], row[2])
			#except:
		 		#pass
		 
read_csv(path)