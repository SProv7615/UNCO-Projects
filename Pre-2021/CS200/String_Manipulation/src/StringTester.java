import input.*;

import bioinformatics.toolkit;

import java.io.IOException;

/*******************************************************************************
 *                           Assignment 4                                       *
 *                                                                              *
 * PROGRAMMER:       Stephen Provost                                            *
 * CLASS:            CS200                                                      *
 * ASSIGNMENT:       Assignment assig-4                                         *
 * INSTRUCTOR:       Dean Zeller                                                *
 * SUBMISSION DATE:  11/1/2019                                                  *
 *                                                                              *
 * DESCRIPTION:                                                                 *
 * Stringing together ATCG's results in plenty of interesting results.          *
 * COPYRIGHT:                                                                   *
 * This program is (c) 2019 Stephen Provost.                                    *
 * This is original work, without use of outside sources.                       *
 *******************************************************************************/

public class StringTester
{
    public static void main(String[] args) throws IOException
    {
        toolkit toolTest = new toolkit();
        RandomInput randTest = new RandomInput();
        //String testReader = test.RequestInfo();
        //System.out.println(testReader);

        /*FileInput textReader = new FileInput();
        toolkit textTester = new toolkit();
        String wolf = textReader.FilePull("C:\\Users\\Styx\\Documents\\CS200\\String_Manipulation\\src\\bioinformatics\\wolf.txt");
        textTester.displayErrors(wolf);
        toolTest.cleanErrors();
        toolTest.generateRNA();
        toolTest.searchSingleSequence("ACG");
        toolTest.searchMultiSequence("ACT");
        toolTest.simpleAnalysis();
        toolTest.mostCommonSequence(10);
        toolTest.removeSequence("ACA");
        toolTest.searchSubsequence("CG");
        toolTest.replaceSequence("ACA","TGT");
        toolTest.toolkitReport();*/

        toolTest.displayErrors("asdfsadwerqrwerqweradACACAGTCGTTACGCACACfsdafazacacac!");
        toolTest.cleanErrors();
        toolTest.generateRNA();
        toolTest.searchSingleSequence("AC");
        toolTest.searchMultiSequence("AC");
        toolTest.simpleAnalysis();
        toolTest.mostCommonSequence(3);
        toolTest.removeSequence("ACA");
        toolTest.searchSubsequence("CG");
        toolTest.replaceSequence("ACA","TGT");
        toolTest.toolkitReport();

        toolkit userTest = new toolkit();
        UserInput inputTest = new UserInput();
        String userData = inputTest.RequestInfo();
        userTest.displayErrors(userData);
        userTest.cleanErrors();
        userTest.generateRNA();
        userTest.searchSingleSequence("ACA");
        userTest.searchMultiSequence("GT");
        userTest.simpleAnalysis();
        userTest.mostCommonSequence(5);
        userTest.removeSequence("GT");
        userTest.searchSubsequence("GTT");
        userTest.replaceSequence("GT","TGT");
        userTest.toolkitReport();

        toolkit randomTester = new toolkit();
        String randomTest = randTest.randInput(10000);
        randomTester.displayErrors(randomTest);
        randomTester.cleanErrors();
        randomTester.generateRNA();
        randomTester.searchSingleSequence("ACA");
        randomTester.searchMultiSequence("GT");
        randomTester.simpleAnalysis();
        randomTester.mostCommonSequence(5);
        randomTester.removeSequence("GT");
        randomTester.searchSubsequence("GTT");
        randomTester.replaceSequence("GT","TGT");
        randomTester.toolkitReport();


    }

}
