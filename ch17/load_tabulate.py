from tabulate import tabulate
import sys, csv

def read_csv(file_name):
    with open(file_name) as file:
        data = [row for row in csv.reader(file, delimiter="|")]
    return data

if __name__ == "__main__":
    data = read_csv(sys.argv[1])
    print(tabulate(data[0:5]))