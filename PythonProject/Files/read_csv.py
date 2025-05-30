import csv

with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip the header row
    print(reader)
    year = dict()
    for row in reader:
        print(row)
        print(row[0], row[1])
        year[row[0]] = row[1]

    print(year) #dict
    print(max(year.values()))

    for key, value in year.items():
        if value == max(year.values()):
            print(f"max month with highest value is: {key} with value {value.strip()}") # strip white spaces from value
