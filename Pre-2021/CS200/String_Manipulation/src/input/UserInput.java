package input;
import java.util.Scanner;
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



public class UserInput
{
    private String strDNAInput;
    Scanner dnaScanner = new Scanner(System.in);

    public String RequestInfo()
    {
        System.out.println("Please input a DNA sequence: ");
        strDNAInput = dnaScanner.nextLine();
        return strDNAInput;
    }
}
