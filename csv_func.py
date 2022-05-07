import csv


def read(filename, list):
    with open(filename, 'r', newline='',  encoding='utf-8') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            list.append(row)


def write(filename, list):
    with open(filename, 'w', newline='',  encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for line in list:
            writer.writerow(line)

def rewrite(filename, newtext):
    temp = []
    read(filename, temp)
    temp.append(newtext)
    write(filename, temp)