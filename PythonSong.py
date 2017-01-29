#Python Song Creator
#Version 1.0
#By Alexander Switzer

#Initialize all of our variables.
theSong = []
fullchorus = ""
lastchorus = ""
spacer = "\n\n\n"

verse1 = raw_input("Enter the first verse: ").upper()
verse2 = raw_input("Enter the second verse: ").upper()
verse3 = raw_input("Enter the third verse: ").upper()
verse4 = raw_input("Enter the fourth verse: ").upper()
chorus = raw_input("Enter the chorus: ").lower()
repeat = int(raw_input("Enter the chorus repeat: "))

#Generate our chorus
for x in xrange(repeat):
    fullchorus += "".join((chorus + " "))

#Sort through our verses for the naughty words- theres probably an easier way to do this...
verse1 = verse1.replace("COOKIES", "_______")
verse2 = verse2.replace("COOKIES", "_______")
verse3 = verse3.replace("COOKIES", "_______")
verse4 = verse4.replace("COOKIES", "_______")
fullchorus = fullchorus.replace("cookies", "_______")

#Assembling our song.
for x in range(1, 3):
    theSong.append(verse1)
    theSong.append(fullchorus)
    theSong.append(verse2)
    theSong.append(fullchorus)
    theSong.append(verse3)
    theSong.append(fullchorus)
    theSong.append(verse4)
    lastchorus = "".join((chorus + " "+ fullchorus))
    theSong.append(lastchorus.lower())
    if x == 1:
        theSong.append("...One more time!...")

#To see the contents of the list.
print spacer
print theSong
print spacer

#Printing out our song.
for item in theSong:
    print item

#Debug
test = raw_input("\nDid it work?: ")
