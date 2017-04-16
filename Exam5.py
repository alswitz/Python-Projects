#Exam 5
#Version 1.0
#By Alexander Switzer

#Import the stuff we are using to make our lives easier
import json

def dataGrabber(query, key):
    petStore = jsonParser() #Calls our other def to populate the program with the json contents.

    for product in petStore: #For x in y
        if key == "k":
            if query.title() in product["Product"]: #If your query is INSIDE any of the strings, return results.
                print "%s - %s" % (product["Product"], product["Price"])
        elif key == "c":
            if query.title() in product["Category"]:
                print "%s - %s" % (product["Product"], product["Price"])
        else:
            print "Nothing Found. :(" #Worse case scenario, no matches.

def jsonParser():
    jsonEncode = ""
    #Take in and make the Json usable for our queries.
    fileIn = open('PetStore.json')
    for line in fileIn:
        line = line.strip()
        jsonEncode = jsonEncode + line
    myJson = json.loads(jsonEncode)

    return myJson

def main():
    #Our main method asks a user for two things. A key and their search.
    searchKey = raw_input("Search by category (c) or keyword (k)?: ")
    if searchKey == "k":
        myQuery = raw_input(("Enter a query for keyword: "))
    elif searchKey == "c":
        myQuery = raw_input(("Enter a query for category: "))

    dataGrabber(myQuery, searchKey) #Pass both along to our grabber which will be doing the Json Searches

    complete = raw_input("Mission Complete.") #So it doesn't instantly close.
main()
