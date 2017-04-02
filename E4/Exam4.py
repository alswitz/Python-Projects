#Exam 4
#Version 1.0
#By Alexander Switzer

#Import the stuff we are using to make our lives easier
import os

def fileReader(keyWord):
    sortedFiles = []
    lineHits = []
    lineCounter = 0
    for files in os.listdir("."):
        if files.endswith(".txt"):
            sortedFiles.append(files)

    for fileName in sortedFiles:
        inFile = open(fileName, 'r')
        for line in inFile:
            if line.find(keyWord.lower()) != -1:
                lineHits.append(line)
                print "%s %s" % (fileName, line)
                lineCounter = lineCounter + 1

    inFile.close()
    print sortedFiles
    print "\n%s RESULTS FOUND FOR  %s" % (lineCounter, keyWord)

def stopProgram():
    raw_input("Mission Complete")

def main():
    input = raw_input("Enter your search term: ")
    fileReader(input)
    stopProgram()

main()
