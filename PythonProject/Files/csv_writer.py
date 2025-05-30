import csv

with open('people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5, 'Anne', 'Paris')
    writer.writerow(csvdata) # tuple or a list
