import pandas as pd
import csv

data1 = []
data2 = []

with open("dataset_2_sorted.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data1.append(i)

with open("final.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data2.append(i)
    

headers1 = data1[0]
planet_data1 = data1[1:]


headers2 = data2[0]
planet_data2 = data2[1:]

headers = headers1 + headers2

planet_data = []
for index, row in enumerate(planet_data2):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("main.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)