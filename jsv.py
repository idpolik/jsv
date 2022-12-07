import json, csv, sys

args = sys.argv

args_csvName= args[1]
args_jsonName= args[2]
args_primaryKey = args[3]

def convert(csv_name:str, json_name:str, primaryKey:str):
    jsonData = {}
    with open (csv_name, 'r', encoding="utf-8") as csv_file:
        csvData = csv.DictReader(csv_file)
        for data_rows in csvData:
            key = data_rows[primaryKey]
            jsonData[key] = data_rows
    
    with open(json_name, 'w') as json_file:
        json.dump(jsonData, json_file, indent=2)

convert(args_csvName, args_jsonName, args_primaryKey)
