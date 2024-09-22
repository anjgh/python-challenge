#create file path across operating systems
import os
#module for reading CSV files
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    