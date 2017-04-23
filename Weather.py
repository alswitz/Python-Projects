#Final Assignment - Weather
#Version 1.0
#By Alexander Switzer

#Import the stuff we are using to make our lives easier
import json
import urllib2

#https://api.apixu.com/v1/current.json?key=ee1281238ce04db79d9151937163103&q=Paris

def dataGrabber(query):
    url = "https://api.apixu.com/v1/current.json?key=ee1281238ce04db79d9151937163103&q=" + query
    jsonTxt = urllib2.urlopen(url).read()
    weatherList = json.loads(jsonTxt)

    if len(weatherList) == 0:
        print "\nNo results for that query. Sorry!"
    else: #print all of our organized JSon after formatting them into a readable state.
        print "\nHere is the current weather for %s, %s" % (weatherList['location']['name'], weatherList['location']['region'])
        print "%s and currently %s degrees (F)." % (weatherList['current']['temp_f'], weatherList['current']['condition']['text'])
        print "It really feels like %s degrees (F) though.\n" %  (weatherList['current']['feelslike_f'])

def main():
    #Our main method asks a user for what they want to search for with error checking.
    checking = True

    MyQuery = raw_input("Enter a zipcode or city name for your weather forecast: \n")
    dataGrabber(MyQuery) #Pass both along to our grabber which will be doing the Json Searches
    restart = raw_input("Would you like to search for another? (y/n): ")

    while(checking):
        if(restart == "y"):
            main()
        elif(restart == "n"):
            print "Okay, good bye!"
            checking = False
        else:
            print "Bad input! Try again."
            restart = raw_input("Check your input! (y/n) only please: ")

main()
