import csv

with open('002_csvfile.csv') as data:
    reader = csv.DictReader(data)
    for row in reader:
        date = row['date']
        convert = float(row['clicks']) / float(row['display'])
        print(f'On {date}, the convert rate is {convert * 100: .2f}%')  # format string
