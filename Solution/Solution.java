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

        Integer sum = 0;

        ArrayList<Integer> currentList = new ArrayList<Integer>(); // List to store the solution

        Integer size = inputList.size();
        Integer i = size - 1;

        // Traverse the Pizza array in reverse order
        for (i = size - 1; i >= 0; i--) {

            // Store the sum temporarily
            Integer tempSum = sum + inputList.get(i);

            if (tempSum == MAX) { // If the temporary sum is equal to target
                sum = tempSum;
                currentList.add(i); // Add current Pizza index to the solution
                return currentList; // Return results

            } else if (tempSum > MAX) { // If the temporary sum is greter than target
                continue; // Try next value

            } else if (tempSum < MAX) { // If the temporary sum is lesser than target
                sum = tempSum;
                currentList.add(i); // Add current Pizza index to the solution
                continue; // Try next value
            }
        }

        return currentList; // Return results
    }

    public static void process(String fileName) throws IOException {

        // Print data to console

        System.out.println("");
        System.out.println("-----------------------");
        System.out.println(fileName);
        System.out.println("-----------------------");

        // Read the input file by name
        BufferedReader fr = new BufferedReader(new FileReader(fileName + ".in"));

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

        // Print input data.

        System.out.println("INPUT");
        System.out.println(MAX + " " + NUM);

        for (Integer input : inputList) {
            System.out.print(input + " ");
        }

        outputList = solve(MAX, inputList); // Solve the problem and get output

        Collections.reverse(outputList); // Reverse the order of the values

        System.out.println("");
        System.out.println("OUTPUT");

        // Create output file.
        try (PrintWriter output = new PrintWriter(fileName + ".out", "UTF-8")) {
            output.println(outputList.size());
            System.out.println(outputList.size());
            for (Integer outputLine : outputList) {
                output.print(outputLine + " ");
                System.out.print(outputLine + " ");
            }
        }
    }
}