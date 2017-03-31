def main():
#Initialize our variables for usage.
    cubeHead = []
    squareMast = []
    advTwister = []
    intTurner = []
    avgMover = []
    pathetic = []

#Temporary array for in loop manipulation
    file = open("timings.txt", "r")
    for line in file:
        temp = line.split(",")
        name = temp[0].rstrip("\n")
        num = float(temp[1].rstrip("\n")) #Strip the valuable components for comparison purposes.
        if num < 9.99:
            cubeHead.append(name)
        elif num == 10 or num < 19.99:
            squareMast.append(name)
        elif num == 20 or num < 29.99:
            advTwister.append(name)
        elif num == 30 or num < 39.99:
            intTurner.append(name)
        elif num == 40 or num < 59.99:
            avgMover.append(name)
        else:
            pathetic.append(name)

    print("--- OFFICIAL RANKINGS --- ")
    print ("\nCube Head (0-9.99): ")
    print cubeHead
    print ("\nSquare Master(10-19.99): ")
    print squareMast
    print ("\nAdvanced Twister(20-29.99): ")
    print advTwister
    print ("\nIntermediate Turner(30-39.99): ")
    print intTurner
    print ("\nAverage Mover(40-59.99)")
    print avgMover
    print ("\nPathetic(60+)")
    print pathetic

    blah = raw_input("\nMission complete. ")

main()
