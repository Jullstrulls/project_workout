import json, os


def load(filename):
    if os.path.exists(filename):    #Return none if file does not exist
        with open(filename, 'r', encoding="utf-8") as f:
            db = json.load(f)
            return db

def appendjson(filename, entry):
    #reads json file and saves in variable data, as list
    with open(filename, "r") as file:
        data = load(filename)
        
    #appends entry on data list
    data.append(entry)

    #writes the new data list to json, overwrites 
    with open(filename, "w") as file:
        json.dump(data, file)
