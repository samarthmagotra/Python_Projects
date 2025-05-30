import csv

people = [['Dan', 34, 'Bucharest'],['Andrei',21, 'London'],['Maria', 45, 'Paris']]

with open('people_2.csv', 'w') as f:
    writer = csv.writer(f, delimiter=':')
    for people in people:
        writer.writerow(people)

with open('people_2.csv', 'r') as f:
    reader = csv.reader(f, delimiter=':')
    print(reader)