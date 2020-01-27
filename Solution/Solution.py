# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   $$$$$$  $$$$$$$$ $$    $$ $$$$$$$$  $$$$$$  $$     $$    $$$$$$$$  $$$$$$$$  $$$$$$  $$     $$    $$$    $$    $$ #
#  $$    $$ $$       $$$   $$ $$       $$    $$ $$     $$    $$     $$ $$       $$    $$ $$     $$   $$ $$   $$$   $$ #
#  $$       $$       $$$$  $$ $$       $$       $$     $$    $$     $$ $$       $$       $$     $$  $$   $$  $$$$  $$ #
#   $$$$$$  $$$$$$   $$ $$ $$ $$$$$$    $$$$$$  $$$$$$$$$    $$     $$ $$$$$$    $$$$$$  $$$$$$$$$ $$     $$ $$ $$ $$ #
#        $$ $$       $$  $$$$ $$             $$ $$     $$    $$     $$ $$             $$ $$     $$ $$$$$$$$$ $$  $$$$ #
#  $$    $$ $$       $$   $$$ $$       $$    $$ $$     $$    $$     $$ $$       $$    $$ $$     $$ $$     $$ $$   $$$ #
#   $$$$$$  $$$$$$$$ $$    $$ $$$$$$$$  $$$$$$  $$     $$    $$$$$$$$  $$$$$$$$  $$$$$$  $$     $$ $$     $$ $$    $$ #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# More Pizza
# Solution for the Practice Round of Google Hash Code 2020
# 27-JAN-2020
# https:#github.com/senesh-deshan/Google-Hash-Code-2020


def solve(MAX, inputList):

    solutionIndexList = [] # To store the best solution indexes through out the solution generating
    solutionValueList = [] # To store the best solution values through out the solution generating
    currentIndexList = [] # To store the current solution indexes through out the solution generating
    currentValueList = [] # To store the current solution values through out the solution generating

    fullSize = len(inputList)

    maxScore = 0 # Stores the maximum score achieved through out the solution generating

    startIndex = fullSize # Stores index which the solution generating should start from

    sum = 0

    # Solution generating starts from the last element of the inputList
    # If first element of currentIndexList becomes 0 that means solution generating is finished

    while((len(currentIndexList) > 0 and currentIndexList[0] != 0) or len(currentIndexList) == 0):

        startIndex = startIndex - 1 

        for i in range(startIndex, -1, -1): # Used to traverse from end to start of the inputList

            currentValue = inputList[i]

            tempSum = sum + currentValue 

            if (tempSum == MAX):  # If the temporary sum is equal to target that means the perfect solution is found
                sum = tempSum
                currentIndexList.append(i) # Add current Pizza index to the solution
                currentValueList.append(currentValue) # Add current Pizza value to the solution
                break  # Go to return solution

            elif (tempSum > MAX):  # If the temporary sum is greter than target
                continue  # Try next value

            elif (tempSum < MAX):  # If the temporary sum is lesser than target
                sum = tempSum
                currentIndexList.append(i) # Add current Pizza index to the solution
                currentValueList.append(currentValue) # Add current Pizza value to the solution
                continue  # Try next value

        if (maxScore < sum):  # If currently generated solution has the best score
            maxScore = sum  # Save its value

            solutionIndexList = []
            solutionValueList = []

            for y in currentIndexList:
                solutionIndexList.append(y)  # Save the currently best solution indexes
            for y in currentValueList:
                solutionValueList.append(y)  # Save the currently best solution values

        if (maxScore == MAX):  # If current solution is the perfect solution
            break # Stop solution generating

        if(len(currentIndexList) == 1): # If solution generating is almost finished
            break # Stop solution generating

        val1 = currentValueList.pop() # Remove the last element from current values
        val2 = currentValueList.pop() # Remove the element before the last element from current values
        sum = sum - (val1 + val2) # Subtract those from sum

        index1 = currentIndexList.pop() # Remove the last element from current indexes
        index2 = currentIndexList.pop() # Remove the element before the last element from current indexes
        startIndex = index2 # Make it as the starting index for the next iteration

    print("SCORE = " + str(maxScore))     # Print the score of the best solution

    return solutionIndexList  # Return indexes list of the best solution


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

    outputList = solve(MAX, inputList)  # Solve the problem and get output

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

