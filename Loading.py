#Opening a csv file
with open("food_prices.csv") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())


import csv
with open("food_prices.csv") as f:
    reader = csv.DictReader(f)
    print(next(reader))
    print(next(reader))    


#Opening an excel file
#pip install xlrd
import xlrd

book = xlrd.open_workbook("cities.xls")
sheet = book.sheet_by_name("Sheet1")
columns = [sheet.cell_value(0, col) for col in range(sheet.ncols)]

for row in range(1, 4):
    row_dict = {}
    for col_index, col_value in enumerate(columns):
        row_dict[col_value] = sheet.cell_value(row, col_index)
    print(row_dict)    


#Opening a JSON file
import json

with open("leia.json") as f:
    leia_data = json.load(f)
leia_data


#Opening an xml file
import xml.etree.ElementTree as ET

tree = ET.parse("leia.xml")
root = tree.getroot()
print("Tree:", tree)
print("Root:", root)
print("Child nodes:")

for child in root:
    if len(list(child)) > 0:
        print(child.tag, "| [", child[0], "... ]")
    elif child.text:
        print(child.tag, "|", child.text)


#Opening a column in aparche parquet
import pyarrow.parquet as pq

table = pq.read_table("colors_and_numbers.parquet", columns=["color"])
table["color"]


#Pickle file
import pickle
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(15)
y = np.random.rand(15)

fig, axes = plt.subplots()
axes.set_xlabel("X Label That Was Set Before Pickling")
axes.scatter(x, y)

pickle.dump(fig, open("plot.pkl", "wb"))

plt.close("all")

with open("plot.pkl", "rb") as f:
    fig = pickle.load(f)
    ax = fig.gca()
    ax.set_ylabel("Y Label That Was Set Later")


#Images
with open("dog.jpg", mode="rb") as f:
    print(f.read(500))