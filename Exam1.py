#Exam 1
#Version 1.0
#By Alexander Switzer
# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    file = open(filename, "r")
    dataArray = []
    for line in file:
        line = float(line)
        dataArray.append(line)
    return dataArray
# ------------------------------------------------------
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
    average = sum(l) / float(len(l))
    return average

# ------------------------------------------------------
# counts and returns the number of values in the
# specified list (l) that are greater than or
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
    speeders = 0
    count = 0
    for item in l:
        if maxSpeed < item:
            speeders = speeders + 1
        else:
            speeders = speeders + 0
    return speeders

# ------------------------------------------------------
# Determines the number of people speeding during
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for
# speeding during rush hour is $150.  The fine for
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    #Import our two files
    fileOne = "data-rush.txt"
    fileTwo = "data-not-rush.txt"

    #Assign variables to hold the data.
    dataSet1 = readData(fileOne) #Rush Hour
    dataSet2 = readData(fileTwo) #Not Rush Hour

    #Create their averagees.
    ave1 = str(round(getAverage(dataSet1), 2))
    ave2 = str(round(getAverage(dataSet2), 2))

    #Count the amount of people who can't drive.
    badDrivers1 = countSpeeders(dataSet1, 69)
    badDrivers2 = countSpeeders(dataSet2, 69)
    rushTickets1 = badDrivers1 * 150
    rushTickets2 = badDrivers2 * 100

    # Print statements
    print "The average speed during rush hour was: %s" % ave1
    print "The average speed not during rush hour was: %s" % ave2
    print "There were %s speeders during rush hour. Total Fine: $%s" % (badDrivers1, rushTickets1)
    print "There were %s speeders not during rush hour. Total Fine: $%s" % (badDrivers2, rushTickets2)
    end = float(raw_input("Mission complete."))

# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()
