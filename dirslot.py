import csv
import os

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

#NO NEED FOR THIS LIST TO BE STORED IN HARD DISK AS AFTER MAKING FOLDER, WE DON'T NEED
#THIS INFORMATION
def makefol(dirstomake):
    curdir = os.getcwd()

    if not os.path.isdir(os.path.join(curdir, "Movies")):
        os.mkdir("Movies")

    moviedir = os.path.join(curdir, "Movies")
    os.chdir(moviedir)

    for i in dirstomake:
        if not os.path.isdir(os.path.join(os.getcwd(), i[0])):
            os.mkdir(i[0])
        datedir = os.path.join(os.getcwd(), i[0])
        os.chdir(datedir)


        if not os.path.isdir(os.path.join(os.getcwd(), i[1])):
            os.mkdir(i[1])

        timedir = os.path.join(os.getcwd(), i[1])
        os.chdir(timedir)


        if not os.path.isdir(os.path.join(os.getcwd(), i[2])):
            os.mkdir(i[2])
        seatsdir = os.path.join(os.getcwd(), i[2])


        os.chdir(datedir)
        os.chdir(moviedir)

    os.chdir(curdir)

def spacetoscore(s):
    snew = ""
    for i in s:
        if(i == " "):
            snew += "_"
        else:
            snew += i
    return snew

