#Python Perfect Shuffler
#Version 1.0
#By Alexander Switzer

#Initialize all of our variables.
rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suit = ["Clubs", "Hearts", "Diamonds", "Spades"]
global shuffleTimes

def buildDeck(rank, suit):
    deck = ["%s of %s" % (x, y) for x in rank for y in suit]
    return deck

def shuffle(deck):
    #Take our to-be deck and split in two even halves.
    FirstH = deck[:26]
    SecondH = deck[26:]
    builtDeck = []
    index = 0

    while index < 52:
        if index % 2 != 0:
            builtDeck.append(FirstH.pop()) #
        else:
            builtDeck.append(SecondH.pop())
        index = index + 1

    builtDeck.reverse() #Finishing our perfect shuffle then returning it.
    return builtDeck

def deal(deck):
    dealtHand = deck[:5] #split and get up to 5.
    return dealtHand

def main():
    deck = buildDeck(rank, suit)
    index = 0

    #Took far longer than I had expected to find a solution to this. Apparently I had to make it a global?
    shuffleTimes = float(raw_input("How many times will you shuffle the deck?: "))
    # while not shuffleTimes.isdigit():
    #     print("Please enter a number ") #Error checking here, apparently it didn't want to work.
    #     shuffleTimes = raw_input("How many times will you shuffle the deck?: ")
    while index < shuffleTimes:
        deck = shuffle(deck)
        index = index + 1

    print("CURRENT DECK: %s \n\n\n\n") % deck #Debug code so I wouldn't go insane.
    print deal(deck)
    missionComplete = raw_input("Mission Complete")

main()
