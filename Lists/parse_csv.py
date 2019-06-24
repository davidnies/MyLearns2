# https://www.youtube.com/watch?v=q5uM4VKywbA

import csv

# 'r' = read
with open('names.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    #  print(csv_reader)
    next(csv_reader)   # skips header row.

    for line in csv_reader:
      #  print(line)
        print(line[2])


'''
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
'''
