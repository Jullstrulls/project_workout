import json, os


def load(filename):
    if os.path.exists(filename):    #Return none if file does not exist
        with open(filename, 'r', encoding="utf-8") as f:
            db = json.load(f)
            return db

def appendjson(filename, entry):
    data = []
    if os.path.exists(filename):
        #reads json file and saves in variable data, as list
        with open(filename, "r") as file:
            data = load(filename)
            
    #appends entry on data list
    data.append(entry)

    #writes the new data list to json, overwrites 
    with open(filename, "w") as file:
        json.dump(data, file)

#checks if username and password exists
def check_login(data, username, password):
    for user in data:
        if user["username"] == username and user["password"] == password:
            return True

def total_weight(data):
    weight = 0
    for workout in data:
        weight += calc_weight_one_workout(workout)
    return weight
        
def weight_month(data, year):
    month = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", "06":"Jun", "07":"Jul", "08":"Apr", "09": "Sep", "10" : "Okt", "11":"Nov", "12" : "Dec"}
    weight_dict = {"Jan":0, "Feb":0, "Mar":0, "Apr":0, "May":0, "Jun":0, "Jul":0, "Aug":0, "Sep":0, "Okt":0, "Nov":0, "Dec":0}
    for workout in data:
        if (workout["date"][:4] == year):
            date = month[workout["date"][5:7]]
            weight_dict[date] += calc_weight_one_workout(workout)
    return weight_dict

def calc_weight_one_workout(workout):
    weight = 0
    for i in range(len(workout["sets"])):
        weight += (int(workout["weight"][i]) * int(workout["reps"][i])) * int(workout["sets"][i])
    return weight

def increase_comparison_last_month(weight_dict):
    procent = {"Jan":0, "Feb":0, "Mar":0, "Apr":0, "May":0, "Jun":0, "Jul":0, "Aug":0, "Sep":0, "Okt":0, "Nov":0, "Dec":0}
    last_month = ""
    for month in weight_dict:
        if month != "Jan":
            if weight_dict[last_month] != 0:
                calc = 100 * ((weight_dict[month] - weight_dict[last_month])//weight_dict[last_month])
                procent[month] = calc
            else:
                procent[month] = "-"
        else:
            procent[month] = "-"
        last_month = month

    return procent
