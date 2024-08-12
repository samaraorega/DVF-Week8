#Opening csv and JSON files
import csv
import json

file_path = ""
file_obj = open(file_path)
file_contents = file_obj.readlines()
file_obj.close()

with open(file_path) as file_obj:
    file_contents = file_obj.readlines()

for line in file_contents:
    print(
        line, end=""
    )  # end="" to avoid double-spacing since strings already end with \n

file_obj.close()       


#Creating a csv file
track_times = [
    [13.10, 13.59, 13.44],
    [13.93, 13.85, 13.47],
    [14.12, 14.41, 13.89],
    [14.42, 13.55, 13.43]
]
print(track_times)

# Initialize an empty string
track_times_csv = ""

# Loop over all lists in the overall list
for index, athlete_times in enumerate(track_times):
    # Join together the values in the nested list using
    # a comma as a separator
    athlete_times_string = ",".join([str(time) for time in athlete_times])
    # Append the values to the overall string
    track_times_csv += athlete_times_string
    # Append a newline, unless this is the last row
    if index < (len(track_times) - 1):
        track_times_csv += "\n"
    
print(track_times_csv)

#Writing a csv into a file
with open("track_times.csv", "w") as f:
    f.write(track_times_csv)

#Desrializing the data back into a list of list
with open("track_times.csv") as f:
    track_times_csv_from_disk = f.read()
print(track_times_csv_from_disk)

track_times_from_disk = []
for row in track_times_csv_from_disk.split("\n"):
    times = [float(time) for time in row.split(",")]
    track_times_from_disk.append(times)
    
track_times_from_disk

#CSV module
#Start by importing it
import csv
#Opening the track times csv using reader()
with open("track_times.csv") as f:
    # Pass the file in to a "reader" object and specify that
    # values without explicit quotes (i.e. all values in this
    # dataset) should be treated as numbers
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    # Get all of the data from the reader using `list`
    track_times_with_csv_module = list(reader)
    
track_times_with_csv_module

#csv.DictReader
#Used with columns that have headings unlike reader()
with open("olympic_medals.csv") as f:
    reader = csv.DictReader(f)
    olympics_data = list(reader)

# Print the first 5 rows of data
for index in range(5):
    print(olympics_data[index])

#.keys() shows what each column represents    