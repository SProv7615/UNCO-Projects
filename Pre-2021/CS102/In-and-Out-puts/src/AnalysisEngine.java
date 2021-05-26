/*******************************************************************************
 *                           Assignment 6                                       *
 *                                                                              *
 * PROGRAMMER:       Stephen Provost                                            *
 * CLASS:            CS102                                                      *
 * ASSIGNMENT:       Assignment assig-6                                         *
 * INSTRUCTOR:       Dean Zeller                                                *
 * SUBMISSION DATE:  3/29/2019                                                  *
 *                                                                              *
 * DESCRIPTION:                                                                 *
 * Writing to and from files. Yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay           *
 *                                                                              *
 * COPYRIGHT:                                                                   *
 * This program is (c) 2019 Stephen Provost and Kevin Ritter. This is original  *
 * work, without use of outside sources.                                        *
 *******************************************************************************/
import javax.lang.model.element.VariableElement;
import java.io.*;
import java.util.*;
import java.lang.Math.*;

public class AnalysisEngine {
    ArrayList<Double> rawData, sortedData;
    ArrayList<String> arrSortedPrinter = new ArrayList<>();
    String studyLeader, studyTitle, studyDate, inputFileName, outputFileName, strCleanData, strSortedData, strTable;
    Double sum, average, variance, stDev, min, max, median;
    Scanner readAEData = new Scanner(System.in);

     /*******************************************************************************
     * Constructor                                                                  *
     *                                                                              *
     * Purpose: CREATE. YOUR. ENGINE!                                               *
     *                                                                              *
     * Parameters:                                                                  *
     *     All of them.                                                             *
     * Return Value: N/A                                                            *
     *******************************************************************************/
    public AnalysisEngine(String studyLeader_, String studyTitle_, String studyDate_, String inputFileName_, String outputFileName_) {
        this.studyLeader = studyLeader_;
        this.studyTitle = studyTitle_;
        this.studyDate = studyDate_;
        this.inputFileName = inputFileName_;
        this.outputFileName = outputFileName_;
        rawData = new ArrayList<Double>();
        sortedData = new ArrayList<Double>();
        sum = 0.0;
        average = 0.0;
        variance = 0.0;
        stDev = 0.0;
        min = 0.0;
        max = 0.0;
        median = 0.0;
    }

     /*******************************************************************************
     * Constructor 2                                                                *
     *                                                                              *
     * Purpose: CREATE. YOUR. ENGINE!                                               *
     *                                                                              *
     * Parameters:                                                                  *
     *     Less of them.                                                            *
     * Return Value: N/A                                                            *
     *******************************************************************************/
    public AnalysisEngine(String inputFileName_, String outputFileName_) {
        this("tempStudyLeader", "tempStudyTitle", "tempStudyDate", inputFileName_, outputFileName_);
        System.out.println("Enter the study leader's name: =>");
        this.studyLeader = readAEData.nextLine();
        System.out.println("Study leader is: " + studyLeader);
        System.out.println();
        System.out.println("Enter the study's title: =>");
        this.studyTitle = readAEData.nextLine();
        System.out.println("Study title is: " + studyTitle);
        System.out.println("");
        System.out.println("Please enter the date: =>");
        this.studyDate = readAEData.nextLine();
        System.out.println("SThe date is set to: " + studyDate);
        //readAEData.close();
    }

     /*******************************************************************************
     * Constructor 3                                                                *
     *                                                                              *
     * Purpose: CREATE. YOUR. ENGINE!                                               *
     *                                                                              *
     * Parameters:                                                                  *
     *     None of them.                                                            *
     * Return Value: N/A                                                            *
     *******************************************************************************/
    public AnalysisEngine() {
        this("tempStudyLeader", "tempStudyTitle", "tempStudyDate",
                "", "tempOutputFileName");
        System.out.println("Enter the study leader's name: =>");
        this.studyLeader = readAEData.nextLine();
        System.out.println("Study leader is: " + studyLeader);
        System.out.println();
        System.out.println("Enter the study's title: =>");
        this.studyTitle = readAEData.nextLine();
        System.out.println("Study title is: " + studyTitle);
        System.out.println("");
        System.out.println("Please enter the date: =>");
        this.studyDate = readAEData.nextLine();
        System.out.println("The date is set to: " + studyDate);
        System.out.println();
        System.out.println("Please enter the location you want files to be pulled from. Add '.txt' to the end of the " +
                "file name.");
        this.inputFileName = readAEData.nextLine();
        System.out.println("The data will be pulled from: " + inputFileName);
        System.out.println();
        System.out.println("Please enter the location you want the datafile to be saved to. Add '.txt' to the end of the " +
                "file name.");
        this.outputFileName = readAEData.nextLine();
        if(!outputFileName.contains(".txt"))
        {
            outputFileName = "DefaultDepository.txt";

        }
        System.out.println("The data will be saved to: " + outputFileName);
    }

     /*******************************************************************************
     * Phase 1                                                                      *
     *                                                                              *
     * Purpose: Gives a bit of info, and if there is no repostiory/depository/name/ *
     * +etc, then it forces the uses to fulfill those.                              *
     * Parameters:                                                                  *
     *     None. Or all. It just depends.                                           *
     * Return Value: N/A                                                            *
     *******************************************************************************/

    public void Phase1() {
        System.out.println("Phase 1: Gathering User Input");
        System.out.println("------------------------------");
        if (!inputFileName.contains(".txt")) {
            Scanner readIntReader = new Scanner(System.in);
            System.out.println("Hello, you silly fool. Rather than importing information from a text file, you must...");
            System.out.println("TYPE IT IN YOURSELF! *Thunder Crashes*");
            System.out.println("I know; a truly horrible fate. Regardless, this is your fate now.");
            System.out.println("Size of Dataset =>");
            String nextLine = readIntReader.nextLine();
            int n = Integer.parseInt(nextLine);
            System.out.println("Data will have " + n + " elements, indexed 0 through " + n);
            System.out.println();
            System.out.println("Please enter integer and floating point values:");
            for (int i = 0; i < n; i++) {
                System.out.println("    Index " + i + ": =>");
                double douNextNum = Double.parseDouble(readIntReader.nextLine());
                rawData.add(douNextNum);
            }
            GetRawData();
            String cleanData = rawData.toString().replace(",", "  ").replace("[", "").replace("]", "").trim();
            System.out.println("Data entered: " + cleanData);
        } else {
            try {
                File filPull = new File(inputFileName);
                Scanner scanData = new Scanner(filPull);
                while (scanData.hasNextLine()) {
                    double douNextNum = Double.parseDouble(scanData.nextLine());
                    rawData.add(douNextNum);
                }
                GetRawData();
                strCleanData = rawData.toString().replace(",", "  ").replace("[", "").replace("]", "").trim();
                System.out.print(strCleanData);
            } catch (FileNotFoundException e) {
                System.out.println("Good job. You broke the system. Now don't you just feel lucky?");
                System.out.println(inputFileName);
                e.printStackTrace();
            }
            System.out.println();
        }
    }

     /*******************************************************************************
     * Phase2                                                                       *
     *                                                                              *
     * Purpose: A method that uses methods. Most of the methods. Plenty of calcs.   *
     *                                                                              *
     * Parameters:                                                                  *
     *     All of them.                                                             *
     * Return Value: N/A                                                            *
     *******************************************************************************/
    public void Phase2() {
        System.out.println("Phase 2: Performing Calculations");
        System.out.println("--------------------------------");
        RawData();
        SortedData();
        CalcSum();
        CalcAverage();
        CalcVariance();
        CalcStDev();
        CalcMin();
        CalcMax();
        CalcMedian();

        System.out.println();
        System.out.println("Phase 2 Completed.");
    }

     /*******************************************************************************
     * GetRawData                                                                   *
     *                                                                              *
     * Purpose: Ensures Raw Data is still usable.                                   *
     *                                                                              *
     * Parameters:                                                                  *
     *     Having Raw Data.                                                         *
     * Return Value: rawData                                                        *
     *******************************************************************************/
    public ArrayList<Double> GetRawData()
    {
        return rawData;
    }

     /*******************************************************************************
     * RawData                                                                      *
     *                                                                              *
     * Purpose: Ensures Raw Data is a string.                                       *
     *                                                                              *
     * Parameters:                                                                  *
     *     Having Raw Data.                                                         *
     * Return Value: None.                                                          *
     *******************************************************************************/
    public void RawData()
    {
        strCleanData = rawData.toString().replace(",", "  ").replace("[", "").replace("]", "").trim();
        System.out.println("    Raw Data:    " + strCleanData);
    }

     /*******************************************************************************
     * SortedData                                                                   *
     *                                                                              *
     * Purpose: Ensures Sorted Data is sorted.                                      *
     *                                                                              *
     * Parameters:                                                                  *
     *     Having Raw Data.                                                         *
     * Return Value: ArrayList of Sorted Data                                       *
     *******************************************************************************/
    public ArrayList<Double> SortedData() {
        sortedData = rawData;
        Collections.sort(sortedData);
        strSortedData = sortedData.toString().replace(",", "  ").replace("[", "").replace("]", "").trim();
        System.out.println("    Sorted Data: " + strSortedData);
        return sortedData;
    }

     /*******************************************************************************
     * CalcSum                                                                      *
     *                                                                              *
     * Purpose: It's a sum. Guess what it is!                                       *
     *                                                                              *
     * Parameters:                                                                  *
     *     An array.                                                                *
     * Return Value: Double                                                         *
     *******************************************************************************/
    public Double CalcSum() {
        for (int i = 0; i < sortedData.size(); i++) {
            sum += sortedData.get(i);
        }
        System.out.println("    Calculated Sum: "+sum);
        return sum;
    }

     /*******************************************************************************
     * CalcAverage                                                                  *
     *                                                                              *
     * Purpose: Calculates the average.                                             *
     *                                                                              *
     * Parameters:                                                                  *
     *     A sum and another num.                                                   *
     * Return Value: average                                                        *
     *******************************************************************************/
    public Double CalcAverage()
    {
        average = sum/sortedData.size();
        System.out.println("    Calculated Average: "+average);
        return average;
    }

     /*******************************************************************************
     * CalcVariance                                                                 *
     *                                                                              *
     * Purpose: Let's get that variance.                                            *
     *                                                                              *
     * Parameters:                                                                  *
     *     An array of data.                                                        *
     * Return Value: Variance.                                                      *
     *******************************************************************************/
    public Double CalcVariance()
    {
        for(int i = 0; i < sortedData.size(); i++)
        {
            variance += (sortedData.get(i) - average) * (sortedData.get(i)-average);
        }
        variance = variance/(sortedData.size()-1);
        System.out.println("    Calculated Variance: "+variance);
        return variance;
    }

     /*******************************************************************************
     * CalcStDev                                                                    *
     *                                                                              *
     * Purpose: Deviations with standards.                                          *
     *                                                                              *
     * Parameters:                                                                  *
     *     Variance. Sqrt'ing.                                                      *
     * Return Value: stDev                                                          *
     *******************************************************************************/
    public Double CalcStDev()
    {
        stDev = Math.sqrt(variance);
        System.out.println("    Calculated Square Root: "+stDev);
        return stDev;
    }

     /*******************************************************************************
     * Min                                                                          *
     *                                                                              *
     * Purpose: The smallest of the small.                                          *
     *                                                                              *
     * Parameters:                                                                  *
     *     Having at least one number.                                              *
     * Return Value: Min                                                            *
     *******************************************************************************/
    public Double CalcMin()
    {
        min = sortedData.get(0);
        System.out.println("    Calculated Minimum: "+ min);
        return min;
    }

     /*******************************************************************************
     * Max                                                                          *
     *                                                                              *
     * Purpose: The biggest of the big.                                             *
     *                                                                              *
     * Parameters:                                                                  *
     *     Having at least one number.                                              *
     * Return Value: Max                                                            *
     *******************************************************************************/

    public Double CalcMax()
    {
        int last = sortedData.size() - 1;
        max = sortedData.get(last);
        System.out.println("    Calculated Maximum: " + max);
        return max;
    }

     /*******************************************************************************
     * Median                                                                       *
     *                                                                              *
     * Purpose: The Middle Number.                                                  *
     *                                                                              *
     * Parameters:                                                                  *
     *     Having at least one number.                                              *
     * Return Value: Median                                                         *
     *******************************************************************************/
    public Double CalcMedian()
    {
        int medianFind;
        medianFind = sortedData.size()/2;
        if(sortedData.size() % 2 == 1)
            median = sortedData.get(medianFind);
        else
        {
            median = (sortedData.get(medianFind -1) + sortedData.get(medianFind))/2;
        }
        System.out.println("    Calculated Median: "+median);
        return median;
    }

     /*******************************************************************************
     * PrintReport                                                                  *
     *                                                                              *
     * Purpose: Let's make this data look perty.                                    *
     *                                                                              *
     * Parameters:                                                                  *
     *     Everything. Literally. Everything.                                       *
     * Return Value: Itself.                                                        *
     *******************************************************************************/
    public ArrayList<String> PrintReport()
    {
        arrSortedPrinter.clear();
        arrSortedPrinter.add(String.format("+------------------------------------------+\n"));
        arrSortedPrinter.add(String.format("|%-42s|\n",studyTitle));
        arrSortedPrinter.add(String.format("|By: %-38s|\n",studyLeader));
        arrSortedPrinter.add(String.format("|Date: %-36s|\n",studyDate));
        arrSortedPrinter.add(String.format("+------------------------------------------+\n"));
        arrSortedPrinter.add(String.format("|Input File:           %20s|\n",inputFileName));
        arrSortedPrinter.add(String.format("|Output File:          %20s|\n", outputFileName));
        arrSortedPrinter.add(String.format("|N:                                   %5d|\n",sortedData.size()));
        arrSortedPrinter.add(String.format("|Sum:                          %12.0f|\n",sum));
        arrSortedPrinter.add(String.format("|Average:                      %12.3f|\n",average));
        arrSortedPrinter.add(String.format("|Variance:                     %12.3f|\n",variance));
        arrSortedPrinter.add(String.format("|Standard Deviation:           %12.3f|\n",stDev));
        arrSortedPrinter.add(String.format("|Minimum:                      %12.3f|\n",min));
        arrSortedPrinter.add(String.format("|Maximum:                      %12.3f|\n",max));
        arrSortedPrinter.add(String.format("|Median:                       %12.3f|\n",median));
        arrSortedPrinter.add(String.format("+------------------------------------------+\n"));
        for(String line: arrSortedPrinter)
        {
            System.out.print(line);
        }
        return arrSortedPrinter;

    }

     /*******************************************************************************
     * Phasetree                                                                    *
     *                                                                              *
     * Purpose: Last and maybe not least.                                           *
     *                                                                              *
     * Parameters:                                                                  *
     *     Having the table.                                                        *
     * Return Value: Nothing                                                        *
     *******************************************************************************/
    public void Phase3()
    {
        System.out.println("Phase 3: Output Table");
        System.out.println("---------------------");
        System.out.println();
        PrintReport();
        System.out.println();
        SavingReport();
    }

     /*******************************************************************************
     * SavingReport                                                                 *
     *                                                                              *
     * Purpose: Saving a report.                                                    *
     *                                                                              *
     * Parameters:                                                                  *
     *     Everything up to this point.                                             *
     * Return Value: N/A                                                            *
     *******************************************************************************/
    public void SavingReport()
    {
        try
        {
            FileWriter wriDepositor = new FileWriter(outputFileName);
            for(String line: arrSortedPrinter)
            {
                wriDepositor.write(line);
                wriDepositor.write(System.lineSeparator());
            }
            wriDepositor.close();
            System.out.println("Successfully wrote to file "+outputFileName);
        }
        catch (IOException e)
        {
            System.out.println("An error has occurred: "+e);
        }
    }

}
