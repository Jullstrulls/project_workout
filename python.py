import json
from api import *
from flask import Flask, render_template, url_for, session, request, redirect, flash
from datetime import timedelta



app = Flask (__name__)
app.secret_key = "whatyouwantsomethinghard"               #to encrypt and decrypt behövs denna för session.
app.permanent_session_lifetime = timedelta(minutes = 5)

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":                           #om ej inloggad, loggar in
        username = request.form["username"]
        password = request.form["password"]                #name value i HTML form input
       
        if username == "Vengeance" and password == "lovejulia":
            session.permanent = True                       #default not permenant, detta gör att längre se ovan
            session["user"] = username
            flash("Login Succesful!")
            return redirect(url_for("home"))
        else:
            flash("Fel inlogg prova igen")
            return render_template("login.html")
        
    elif "user" in session:                                 #om inloggad men går tillbaka, redirect till inloggad
        flash("Already logged in!")
        return redirect(url_for("home"))
            
    else:
        return render_template("login.html")

@app.route("/home")
def home():
    if "user" in session:
        user = session["user"]
        return render_template("home.html", user = user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:          #bara skriva meddelandet om användare inloggad
        user = session["user"]
        flash(f"{user} have been logged out", "info")               #varning, info and error. Kategorier
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/add_workout", methods=["POST", "GET"])
def add_workout():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            name = request.form["name"]
            date = request.form["date"]
            descr = request.form["descr"]
            exercise = [request.form["exercise"],request.form["exercise1"],request.form["exercise2"]]
            sets = [request.form["sets"],request.form["sets1"],request.form["sets2"]]
            reps = [request.form["reps"],request.form["reps1"],request.form["reps2"]]
            weight = [request.form["weight"],request.form["weight1"],request.form["weight2"]]

            
            new_workout = {"name":name,"date":date, "descr":descr, "exercise":exercise, "sets":sets, "reps":reps, "weight":weight}
            appendjson("data.json", new_workout)
            
            return render_template("add_workout.html")
        else:
            return render_template("add_workout.html")
    else:
        flash("you are not logged in")
        return redirect(url_for("login"))

@app.route("/workouts")
def workout():
    if "user" in session:
        user = session["user"]
        data = load("data.json")
        return render_template("workout.html", data=data)
    else:
        flash("you are not logged in")
        return redirect(url_for("login"))





##################################
#SKAPA DATALAGER
##################################






# with open("data.json") as f:
#    data = json.load(f)

# for user in data["users"]:
#      del user["city"]

# with open("new_data.json", "w") as f:
#     json.dump(data, f, indent = 2)


    
if __name__ == "__main__":
    app.run(debug=True)                                #debug true gör att uppdateras hela tiden
