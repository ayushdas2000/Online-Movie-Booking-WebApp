from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import secrets
# from forms import signupform, loginform

from dir import writecsv, readcsv
from dirslot import readslots, writeslots, makefol, spacetoscore

app = Flask(__name__)

#Cookie Stuff
#Setting a key for the user to remember that he is logged in
# app.config['SECRET_KEY'] = secrets.token_hex(16)

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


################
#THE ADMIN PAGES
################

gr = []
readslots(gr)

dirstomake =[]


@app.route("/admin")
def options():
    return render_template("options.html")

@app.route("/addmovie")
def addmovie():
    return render_template("addmov.html")

@app.route("/slotsel", methods = ["POST"])
def slotsel():
    moviename = request.form.get("moviename")
    movdirector = request.form.get("movdirector")
    leadactor = request.form.get("leadactor")
    rating = request.form.get("rating")

    l = [moviename, movdirector, leadactor, rating]

    with open("movieinfo.csv", "a") as movinfo:
        writeinfo = csv.writer(movinfo)
        writeinfo.writerow(l)

    return render_template("slot.html", gr = gr, moviename = moviename)

@app.route("/movieadded", methods = ["POST"])
def added():
    lis = request.form.getlist("sl")
    # print (list)
    name = request.form.get("moviename")
    name = spacetoscore(name)

    for i in lis:
        ct = 0
        j = i[ct]
        while(j != '-' and ct < len(i)):
            ct += 1
            j = i[ct]
        gr[int(i[0:ct])][int(i[ct+1:len(i)])] = name

        #The following list is of type [mname, date, slot]
        addu = [name, gr[int(i[0:ct])][0], "s" + str(int(i[ct+1:len(i)]))]
        dirstomake.append(addu)

    makefol(dirstomake)

    # print(dirstomake)
    writeslots(gr)
    return "<h1>Movie Added Succesfully</h1>"


###############
#THE USER PAGES
###############


#The seats are 200 in number, 100-100 divided
#allseats is a 2D list representing seats with a gap

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/displaymov")
def viewmov():
    lis = []
    if(os.path.exists("movieinfo.csv")):
        with open("movieinfo.csv", "r") as read:
            rd = csv.reader(read)
            for line in rd:
                lis.append(line)

        return render_template("viewmovies.html", lis = lis)
    else:
        return "<h1>NO MOVIES TO DISPLAY<h1>"

@app.route("/movies")
def selmov():
    #read dirs before selecting movie
    movs = readcsv()
    #passed the whole dictionary to template to access its keys that are movies
    return render_template("movies.html", movs = movs)

movs = readcsv()

@app.route("/movies/date", methods=["POST"])
def seldate():
    movs = readcsv()
    #accessed the things that form at /movies gave to the date, i.e. the movie selected
    selmovie = request.form.get("movie")

    #two arguments are given to render with template, one is to get the options of dates
    #available to select one and other is the name of movie to just propogate
    return render_template("date.html", dates = movs[selmovie], selmovie = selmovie)

movs = readcsv()

@app.route("/movies/date/time", methods=["POST"])
def seltime():
    movs = readcsv()
    seldate = request.form.get("date")
    selmovie = request.form.get("selectedmovie")
    return render_template("time.html", times = movs[selmovie][seldate], selmovie=selmovie, seldate=seldate)

movs = readcsv()

@app.route("/movies/date/time/seats", methods=["POST"])
def seats():
    movs = readcsv()
    seltime = request.form.get("time")
    seldate = request.form.get("selecteddate")
    selmovie = request.form.get("selectedmovie")
    return render_template("seatmat.html", allseats= allseats, bookeds = movs[selmovie][seldate][seltime], seltime=seltime, selmovie=selmovie, seldate=seldate)

movs = readcsv()

@app.route("/movies/date/time/seats/registered", methods=["POST"])
def register():
    movs = readcsv()
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

movs = readcsv()

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
