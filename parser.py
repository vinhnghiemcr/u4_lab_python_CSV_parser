####################################################
#  python library imports here: csv, json
import csv
import json


####################################################
# Set up 3 global variables to process the csv file
# and convert it to JSON
# All variables will be empty lists to start: []

read_data = []
# for CSV data read and stored as tuples
fields = []
# for the name of each column in the CSV file's rows
employee_list = []
# for formatted data, a dictionary for each row in the CSV file


####################################################
# main function
# Takes in the path of the csv file and an output path
# for creating a new JSON file as arguments
# creates a new JSON file with formatted csv data

def csv_to_json(csv_path, json_path):
    with open(csv_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for entry in csv_data:
            read_data.append(tuple(entry))
    headers = read_data[0]
    employees = [read_data[index] for index in range(1, len(read_data))]
    for name in headers:
        fields.append(name.replace(' ', '_').lower())

    for employee in employees:
        employee_json = {}
        for i in range(len(employee)):
            employee_json[fields[i]] = employee[i]
        employee_list.append(employee_json)

    with open(json_path, mode='w') as output_file:
        json.dump(employee_list, output_file, indent=2)


csv_to_json('data/employee_data.csv', 'data/employees.json')
print(employee_list[1])
print(employee_list[2])
