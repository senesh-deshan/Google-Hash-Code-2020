# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   $$$$$$  $$$$$$$$ $$    $$ $$$$$$$$  $$$$$$  $$     $$    $$$$$$$$  $$$$$$$$  $$$$$$  $$     $$    $$$    $$    $$ #
#  $$    $$ $$       $$$   $$ $$       $$    $$ $$     $$    $$     $$ $$       $$    $$ $$     $$   $$ $$   $$$   $$ #
#  $$       $$       $$$$  $$ $$       $$       $$     $$    $$     $$ $$       $$       $$     $$  $$   $$  $$$$  $$ #
#   $$$$$$  $$$$$$   $$ $$ $$ $$$$$$    $$$$$$  $$$$$$$$$    $$     $$ $$$$$$    $$$$$$  $$$$$$$$$ $$     $$ $$ $$ $$ #
#        $$ $$       $$  $$$$ $$             $$ $$     $$    $$     $$ $$             $$ $$     $$ $$$$$$$$$ $$  $$$$ #
#  $$    $$ $$       $$   $$$ $$       $$    $$ $$     $$    $$     $$ $$       $$    $$ $$     $$ $$     $$ $$   $$$ #
#   $$$$$$  $$$$$$$$ $$    $$ $$$$$$$$  $$$$$$  $$     $$    $$$$$$$$  $$$$$$$$  $$$$$$  $$     $$ $$     $$ $$    $$ #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import sys

# More Pizza
# Solution for the Practice Round of Google Hash Code 2020
# 27-JAN-2020
# https:#github.com/senesh-deshan/Google-Hash-Code-2020


def solve(target, inputList, length):

    current = [] # To store the current solution indexes through out the solution generating
    maxScore = 0 # Stores the maximum score achieved through out the solution generating
    sum = 0

    # Solution generating starts from the last element of the inputList
    # If first element of current becomes 0 that means solution generating is finished

    while((len(current) > 0 and current[0] != 0) or len(current) == 0):

        length = length - 1 

        # Used to traverse from end to start of the inputList
        for i in range(length, -1, -1):

            currentValue = inputList[i]

            tempSum = sum + currentValue 

            if tempSum <= target:
                sum = tempSum
                current.append(i) # Add current Pizza index to the solution

                # If the temporary sum is equal to target that means the perfect solution is found
                if (tempSum == target):
                    return current, sum

        # If currently generated solution has the best score
        if (maxScore < sum):  
            maxScore = sum  # Save its value
            solution = current.copy()

        # remove smaller number and try even smaller ones
        if(len(current) != 0):
            lastIndex = current.pop()
            sum = sum - inputList[lastIndex]
            length = lastIndex # Make it as the starting index for the next iteration

        # If solution generating is almost finished
        if(len(current) == 0 and (length == 0)): 
            break # Stop solution generating

    # Return indexes list of the best solution
    return solution, maxScore


def process(fileName):

    # Print data to console
    print("")
    print("-----------------------")
    print(fileName)
    print("-----------------------")

    #  Read the open file by name
    inputFile = open(inputFilesDirectory + fileName + ".in", "rt")

    #  Read file
    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()


    #  Print input data
    print("INPUT")
    print(firstLine)
    print(secondLine)

    #  Assign parameters
    MAX, NUM = list(map(int, firstLine.split()))

    #  Create the pizza list by reading the file
    inputList = list(map(int, secondLine.split()))

    outputList, sum = solve(MAX, inputList, NUM)  # Solve the problem and get output

    #  Print output data and create output file
       
    print("")
    print("OUTPUT")
    print(len(outputList))

    outputString = ""
    for l in outputList:
        outputString = outputString + str(l) + " "
    print(outputString)

    outputFile = open(outputFilesDirectory + fileName + ".out", "w")
    outputFile.write(str(len(outputList)) + "\n")
    outputFile.write(outputString)
    outputFile.close()


inputFilesDirectory = "Input/"  # Location of input files
outputFilesDirectory = "Output/"  # Location of output files

fileNames = ["a_example", "b_small", "c_medium",
             "d_quite_big", "e_also_big"]  # File names

for fileName in fileNames:  # Take each and every file and solve
    process(fileName)

