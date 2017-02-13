#Python Temperature Analytical Machine
#Version 1.0
#By Alexander Switzer

#Read in our temperatures from a file, set to read only.
def readTemps():
    file = open("temps.txt", "r")
    tempArray = []
#Put them into an array line by line.
    for line in file:
        line = float(line)
        tempArray.append(line)
    return tempArray

#Calculate the average of a certain range of years.
def calculateAve(temps, start, stop):
    aveArray = []
    count = 0
    average = 0
    for item in temps:
        if count >= start and count < stop:
            count = count + 1
            aveArray.append(item)
        else:
            count = count + 1
    average = sum(aveArray) / float(len(aveArray))
    return average

#Count the instances of a positive #
def count(temps, start, stop):
    plusCount = 0
    count = 0
    for item in temps:
        if count >= start and count < stop:
            count = count + 1
            if item > 0:
                plusCount = plusCount + 1
        else:
            count = count + 1
    return plusCount

def main():
    temps = readTemps()
    average1 = calculateAve(temps, 0, 81)
    print "During the first 81 years, the average deviation of the temperature anomaly is %s" % average1
    count1 = count(temps, 0, 81)
    print "During the first 81 years, %s had a positive temperature anomaly." % count1
    average1 = calculateAve(temps, 81, 116)
    print "During the last 35 years, the average deviation of the temperature anomaly is %s" % average1
    count1 = count(temps, 81, 116)
    print "During the last 35 years, %s had a positive temperature anomaly." % count1
    print "\n"
    end = float(raw_input("Mission complete."))
main()
