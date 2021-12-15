import pandas as pd
import csv

data = []

with open("dataset_2.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)

headers = data[0]
planet_data = data[1:]

for row in planet_data:
    row[2] = row[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("dataset_2_sorted.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)