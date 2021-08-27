from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import secrets
# from forms import signupform, loginform

from dir import writecsv, readcsv

def readslots(gr):
    with open("slots.csv", "r") as slots:
    	file_reader = csv.reader(slots)
    	for line in file_reader:
    		gr.append(line)

def writeslots(gr):
	with open("slots.csv", "w") as slots:
		file_writer = csv.writer(slots)

		for i in gr:
			file_writer.writerow(i)












gr = []
readslots(gr)


















app = Flask(__name__)

#Cookie Stuff
#Setting a key for the user to remember that he is logged in
app.config['SECRET_KEY'] = secrets.token_hex(16)

allseats = [];
for i in range(10):
    row = []
    col1 = []
    for j in range(10):
        col1.append(str(i) + "-" + str(j))
    row.append(col1)

    col2 = []
    for j in range(10, 20):
        col2.append(str(i) + "-" + str(j))
    row.append(col2)
    allseats.append(row)

movs = readcsv()

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/movies")
def selmov():
    #passed the whole dictionary to template to access its keys that are movies
    return render_template("movies.html", movs = movs)

@app.route("/movies/date", methods=["POST"])
def seldate():
    #accessed the things that form at /movies gave to the date, i.e. the movie selected
    selmovie = request.form.get("movie")

    #two arguments are given to render with template, one is to get the options of dates
    #available to select one and other is the name of movie to just propogate
    return render_template("date.html", dates = movs[selmovie], selmovie = selmovie)


@app.route("/movies/date/time", methods=["POST"])
def seltime():
    seldate = request.form.get("date")
    selmovie = request.form.get("selectedmovie")
    return render_template("time.html", times = movs[selmovie][seldate], selmovie=selmovie, seldate=seldate)


@app.route("/movies/date/time/seats", methods=["POST"])
def seats():
    seltime = request.form.get("time")
    seldate = request.form.get("selecteddate")
    selmovie = request.form.get("selectedmovie")
    return render_template("seatmat.html", allseats= allseats, bookeds = movs[selmovie][seldate][seltime], seltime=seltime, selmovie=selmovie, seldate=seldate)

@app.route("/movies/date/time/seats/registered", methods=["POST"])
def register():
    inlist = request.form.getlist("ts")
    seltime = request.form.get("selectedtime")
    seldate = request.form.get("selecteddate")
    selmovie = request.form.get("selectedmovie")

    if(request.method == "POST"):
        if(len(inlist) == 0):
            return "<h1>Please go back and select seats<h1>"
        else:
            movs[selmovie][seldate][seltime].extend(inlist)
    writecsv(movs)
    return render_template("success.html")




















@app.route("/addmovie")
def addmovie():
    return render_template("addmov.html")

@app.route("/slotsel", methods = ["POST"])
def slotsel():
    request.form.get("moviename")
    return render_template("slot.html", gr, moviename = moviename)


# @app.route("/signup")
# def signup:
#     #making a signupform object
#     form = signupform()
#     return render_template('signupp.html', title = "Sign Up", form = form)


# @app.route("/loginuser")
# def userlog:
#     #making a loginform object
#     form = loginform()
#     return render_template('loginn.html', title = "Log in", form = form)

# @app.route("/loginadmin")
# def adminlog:

if(__name__ == "__main__"):
    app.run()
