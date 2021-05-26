package input;
import java.util.Random;
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

public class RandomInput
{
    Scanner randScanner = new Scanner(System.in);
    int randNum = 0;
    Random GenNum = new Random();
    StringBuilder dnaChain = new StringBuilder();
    String strDNAInput, strDNAChain;

    public String randInput()
    {
        System.out.println("Please input the desired length of a randomly created DNA strand: ");
        String readNum = randScanner.nextLine();
        int dnaLength = Integer.parseInt(readNum);
        for(int i = 0; i<dnaLength;i++)
        {
            dnaChain.append(randDNA());
        }
        strDNAInput = dnaChain.toString();
        return strDNAInput;
    }

    public String randInput(int userInput_)
    {
        int dnaLength = userInput_;
        for(int i = 0; i<dnaLength;i++)
        {
            dnaChain.append(randDNA());
        }
        return strDNAChain = dnaChain.toString();
    }

    public StringBuilder randOutput()
    {
        return dnaChain;
    }

    private Integer randGen()
    {
        randNum = GenNum.nextInt(4);
        return randNum;
    }

    private String randDNA()
    {
        randGen();
        String nextDNA = "";
        if(randNum == 0)
        {
            nextDNA = "A";
        }
        else if(randNum==1)
        {
            nextDNA = "C";
        }
        else if(randNum==2)
        {
            nextDNA = "G";
        }
        else if(randNum==3)
        {
            nextDNA = "T";
        }
        return nextDNA;
    }


}
