#Json Assignment
#Version 1.0
#By Alexander Switzer

#Import the stuff we are using to make our lives easier
import json

def dataGrabber(query):
    studentList = jsonParser()

    for student in studentList:
        if student["Name"] == query.title():
            print "%s - %s" % (student["Name"], student["Class Status"])
            print "Course Schedule: %s" % student["Courses"]
            print "Current GPA: %s" % student["GPA"]

def jsonParser():
    jsonEncode = ""

    fileIn = open('myJson.json')
    for line in fileIn:
        line = line.strip()
        jsonEncode = jsonEncode + line
    myJson = json.loads(jsonEncode)

    return myJson

def main():
    myQuery = raw_input(("Enter a query for student schedules (FALL 2017): "))
    dataGrabber(myQuery)

    complete = raw_input("Mission Complete.")
main()
