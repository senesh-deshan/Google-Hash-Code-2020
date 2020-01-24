////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//  ######  ######## ##    ## ########  ######  ##     ##    ########  ########  ######  ##     ##    ###    ##    ## //
// ##    ## ##       ###   ## ##       ##    ## ##     ##    ##     ## ##       ##    ## ##     ##   ## ##   ###   ## //
// ##       ##       ####  ## ##       ##       ##     ##    ##     ## ##       ##       ##     ##  ##   ##  ####  ## //
//  ######  ######   ## ## ## ######    ######  #########    ##     ## ######    ######  ######### ##     ## ## ## ## //
//       ## ##       ##  #### ##             ## ##     ##    ##     ## ##             ## ##     ## ######### ##  #### //
// ##    ## ##       ##   ### ##       ##    ## ##     ##    ##     ## ##       ##    ## ##     ## ##     ## ##   ### //
//  ######  ######## ##    ## ########  ######  ##     ##    ########  ########  ######  ##     ## ##     ## ##    ## //
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// More Pizza
// Solution for the Practice Round of Google Hash Code 2020
// 20-JAN-2020
// https://github.com/senesh-deshan/Google-Hash-Code-2020

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;

class Solution {

    static int MAX;
    static int NUM;
    static ArrayList<Integer> inputList;
    static ArrayList<Integer> outputList;
    static String inputFilesDirectory = "../Input/"; // Location of input files
    static String outputFilesDirectory = "../Output/"; // Location of output files

    public static void main(String[] args) throws IOException {

        // Begin solving
        String[] fileNames = { "a_example", "b_small", "c_medium", "d_quite_big", "e_also_big" }; // File names list

        for (String fileName : fileNames) { // Take every file and solve
            inputList = new ArrayList<Integer>();
            outputList = new ArrayList<Integer>();
            process(fileName);
        }

    }

    public static ArrayList<Integer> solve(Integer MAX, ArrayList<Integer> inputList) {

        ArrayList<Integer> solutionList = new ArrayList<Integer>(); // List to store the best solution

        Integer fullSize = inputList.size();
        Integer i;
        Integer j;
        Integer maxScore = 0;

        // Decrease the traversable size of the initial Pizza array in reverse order, by
        // 1 in each iteration
        for (j = fullSize - 1; j >= 0; j--) {

            Integer size = j;
            // Integer previousValue = 0;
            Integer sum = 0;
            ArrayList<Integer> currentList = new ArrayList<Integer>(); // List to store the solution at each iteration
                                                                       // of the loop

            // Traverse the current Pizza array in reverse order
            for (i = size; i >= 0; i--) {

                Integer currentValue = inputList.get(i);

                // Store the sum temporarily
                Integer tempSum = sum + currentValue;

                if (tempSum == MAX) { // If the temporary sum is equal to target
                    sum = tempSum;
                    currentList.add(i); // Add current Pizza index to the solution
                    break; // Go to return solution

                } else if (tempSum > MAX) { // If the temporary sum is greter than target
                    continue; // Try next value

                } else if (tempSum < MAX) { // If the temporary sum is lesser than target
                    sum = tempSum;
                    currentList.add(i); // Add current Pizza index to the solution
                    continue; // Try next value
                }
            }

            if (maxScore < sum) { // If current solution is the best
                maxScore = sum; // Keep its value
                solutionList = currentList; // Keep the solution
            }
        }

        // Print the score of the best solution (AKA the maximum number of slices)
        System.out.println("");
        System.out.println("");
        System.out.print("SCORE = ");
        System.out.println(maxScore);

        return solutionList; // Return best solution
    }

    public static void process(String fileName) throws IOException {

        // Print data to console

        System.out.println("");
        System.out.println("-----------------------");
        System.out.println(fileName);
        System.out.println("-----------------------");

        // Read the input file by name
        BufferedReader fr = new BufferedReader(new FileReader(inputFilesDirectory + fileName + ".in"));

        String line, firstLine;
        firstLine = fr.readLine();

        String[] vars;
        vars = firstLine.split(" ");

        // Assign constraints
        MAX = Integer.valueOf(vars[0]); // Maximum Pizza slices requires
        NUM = Integer.valueOf(vars[1]); // Number of Pizzas available

        // Create the pizza list by reading the file
        while ((line = fr.readLine()) != null) {
            String letters[] = line.split(" ");
            for (String letter : letters) {
                inputList.add(Integer.valueOf(letter));
            }
        }

        fr.close();

        // Print input data

        System.out.println("INPUT");
        System.out.println(MAX + " " + NUM);

        for (Integer input : inputList) {
            System.out.print(input + " ");
        }

        outputList = solve(MAX, inputList); // Solve the problem and get output

        Collections.reverse(outputList); // Reverse the order of the values

        System.out.println("");
        System.out.println("OUTPUT");

        // Print output data and create output file
        try (PrintWriter output = new PrintWriter(outputFilesDirectory + fileName + ".out", "UTF-8")) {
            output.println(outputList.size());
            System.out.println(outputList.size());
            for (Integer outputLine : outputList) {
                output.print(outputLine + " ");
                System.out.print(outputLine + " ");
            }
        }

        System.out.println("");
    }
}