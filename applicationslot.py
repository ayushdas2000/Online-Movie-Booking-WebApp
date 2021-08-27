from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import secrets
# from forms import signupform, loginform

from dir import writecsv, readcsv
from dirslot import readslots, writeslots, makefol

gr = []
readslots(gr)

dirstomake =[]

app = Flask(__name__)

@app.route("/")
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
    list = request.form.getlist("sl")
    # print (list)
    name = request.form.get("moviename")
    for i in list:
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


if(__name__ == "__main__"):
    app.run()
