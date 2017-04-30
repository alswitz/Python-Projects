#Exam 6
#Version 1.0
#By Alexander Switzer

#Import the stuff we are using to make our lives easier
#This was one of the easier programs, so it'd be even more work to split them up into smaller defs.
def main():
    potentialSuspects = ['Miss Scarlet', 'Col Mustard', 'Mr Green']
    potentialWeapons = ['Candlestick', 'Wrench', 'Pipe']
    possibilities = len(potentialSuspects) * len(potentialWeapons)

    while(possibilities > 1): #While possibilities are greater than 1, enter your clues to have possibilities depleted!
        print "There are %s possibilities left.\n" % possibilities
        userInput = raw_input("Is the clue about a weapon or suspect? (w) or (s): ").title()
        if userInput == "W":
            print potentialWeapons
            myQuery = raw_input("Please enter the weapon you found a clue for: ").title()
            potentialWeapons.remove(myQuery)
        elif userInput == "S":
            print potentialSuspects
            myQuery = raw_input("Please enter the suspect you found a clue for: ").title()
            potentialSuspects.remove(myQuery)
        else:
            print "Invalid query."

        print "\nThere are %s possibilities left." % possibilities
        if(possibilities == 1):
            print "The culprit is %s who used a %s as the murder weapon!" % (potentialSuspects[0], potentialWeapons[0]) #Since there is only one possibility left, print the combination of the two lists with one entry each.

main()
