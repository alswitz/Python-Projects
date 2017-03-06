#Hotdog Contest
#Version 1.0
#By Alexander Switzer

#Import the stuff we are using to make our lives easier
import random
import time

def main():
    #setting some variables for use
    goal = 50
    game = False
    p1 = p2 = p3 = turn = 0
    lossText = "Your guess was incorrect! Sorry!"
    winText = "Your guess was correct by the way! Good Job!"

    choice = raw_input("Enter who you think will win? Fred, Sally or Tom\n")
    if(choice == "Sally" or choice == "Fred" or choice == "Tom"):
        game = True
        print "\nGAME START!"
    else:
        choice = raw_input("Enter Sally, Fred or Tom in order to proceed.")

    while game:
        time.sleep(2)
        turn = turn + 1
        p1 = p1 + random.randint(0, 5)
        p2 = p2 + random.randint(0, 5)
        p3 = p3 + random.randint(0, 5)

        print "\n**INTENSE BOUT OF HOTDOG MUNCHING***\n"
        print "Turn #%s\n" % turn
        print "Sally: %s hotdogs eaten!" % p1
        print "Tom: %s hotdogs eaten!" % p2
        print "Fred: %s hotdogs eaten!" % p3

        #Check if P1 has won.
        if(p1 >= 50):
            game = False
            print "\nSally has won!"
            if(choice == "Sally"):
                print winText
            else:
                print lossText

        #Check if P2 has won.
        if(p2 >= 50):
            game = False
            print "\nTom has won!"
            if(choice == "Tom"):
                print winText
            else:
                print lossText

        #Check if P3 has won.
        if(p3 >= 50):
            game = False
            print "\nFred has won!"
            if(choice == "Fred"):
                print winText
            else:
                print lossText

    blah = raw_input("\nMission complete.")

main()
