import csv

with open('passwd.csv','r') as f:
    #reader = csv.reader(f)
    reader = csv.reader(f, delimiter=':', lineterminator='\n') #seperating by :
    print(reader)
    for row in reader:
        print(row)

# dialect in csv
print(csv.list_dialects())
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

with open('items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')
    for row in reader:
        print(row)

## Appending a line to the csv file
with open('items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))