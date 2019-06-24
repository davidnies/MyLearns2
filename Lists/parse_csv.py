# https://www.youtube.com/watch?v=q5uM4VKywbA

import csv


with open('names.csv', 'r') as csv_file:   # 'r' = read
    # csv_reader = csv.reader(csv_file)
    #
    #
    # with open('new_names.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')
    #
    #     for line in csv_reader:
    #         csv_writer.writerow(line)

    csv_reader = csv.DictReader(csv_file)
    # for line in csv_reader:
    #     print(line['email'])   #'email' - is the key in the Dictionary


    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
    #
