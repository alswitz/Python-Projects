#Bird Dictionary
#Version 1.0
#By Alexander Switzer
# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen
# most often.  If there is a tie, print all of birds that are
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary
# whose keys are bird names and whose values are the number of
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds(filename):
    file = open(filename, "r")
    dictionary = {}
    for line in file:
        temp = line.split(",")
        name = temp[0].rstrip("\n")
        num = int(temp[1].rstrip("\n"))
        if name in dictionary:
            dictionary[name] = dictionary[name] + num
            print "Duplicate key detected for %s, adding values." % name
        else:
            dictionary[name] = num
    print "Dictionary created. \nTotal values for all birds combined: %s\n\n" % sum(dictionary.values())
    return dictionary
# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up
# the sighting count for that bird in the specified
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    searchFor = raw_input("Please enter the bird you would like to find: ")
    result = d.get(searchFor.title())
    print "%s spottings found for %s" % (result, searchFor.title())
    return

def main():
    fileOne = "Birds.txt"
    birdDict = countBirds(fileOne)
    askUser(birdDict)

    blah = raw_input("Mission complete. ")

main()
