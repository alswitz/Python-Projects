#Exam 3
#Version 1.0
#By Alexander Switzer

#Import the stuff we are using to make our lives easier
def main():
    import random
    import time

    game = True #Game time!
    count = 1 #Our counter for attempts

    choices = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab', 'bird']
    random.shuffle(choices)

    print choices #Debug
    while game == True:
        print "\n*** ROUND #%s ! ***" % count
        print "Please enter choice #1 (between 0-9):"
        input1 = int(raw_input())
        while input1 < 0 or input1 > 9:
            print "\nPay attention. Invalid choice!"
            print "Please enter choice #1 (between 0-9):"
            input1 = int(raw_input())

        print "\nOkay, now please enter choice #2 (between 0-9):"
        input2 = int(raw_input())
        while input2 < 0 or input2 > 9 and input2 != input1:
            print "\nPay attention. Invalid choice!"
            print "Please enter choice #2 (between 0-9):"
            input2 = int(raw_input())

        if(choices[input1] == choices[input2]):
            print "\nYou were correct! Good job!"
            print "It took %s tries!" % count
            game = False
        else:
            print "Sorry, no dice!"
            print "Card #1 = %s" % choices[input1]
            print "Card #2 = %s" % choices[input2]
            count = count + 1

    print "Mission complete."
    end = int(raw_input())

main()
