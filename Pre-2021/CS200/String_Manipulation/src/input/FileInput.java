package input;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
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

public class FileInput
{
    String strDNAInput;
    Scanner textReader = new Scanner(System.in);
    public String FilePull(String fileName_)
    {
        try
        {
            File DNAText = new File(fileName_);
            Scanner fileReader = new Scanner(DNAText);
            while(fileReader.hasNextLine())
            {
                strDNAInput=fileReader.nextLine();
            }
        }
        catch(IOException e)
        {
            System.out.println("Terribly sorry, but it seems that the file does not exist.");
        }
        return strDNAInput;
    }

    public String FilePull()
    {
        try
        {
            System.out.println("Please input a file name: ");
            String readInput = textReader.nextLine();
            File DNAText = new File(readInput);
            Scanner fileReader = new Scanner(DNAText);
            while(fileReader.hasNextLine())
            {
                strDNAInput+=fileReader.nextLine();
            }
        }
        catch(IOException e)
        {
            System.out.println("Terribly sorry, but it seems that the file does not exist.");
        }
        return strDNAInput;
    }

    public void FileSend(String fileOutputName_, String dnaToWrite_) throws IOException
    {
        BufferedWriter dnaWriter = new BufferedWriter(new FileWriter(fileOutputName_));
        dnaWriter.write(dnaToWrite_);
        System.out.println("DNA Recorded to "+fileOutputName_);
        dnaWriter.close();
    }

    public void FileSend(String fileOutputName_, String rawdnaToWrite, String dnaToWrite_, String rnaToWrite) throws IOException
    {
        BufferedWriter dnaWriter = new BufferedWriter(new FileWriter(fileOutputName_));
        dnaWriter.write(rawdnaToWrite);
        dnaWriter.newLine();
        dnaWriter.write(dnaToWrite_);
        dnaWriter.newLine();
        dnaWriter.write(rnaToWrite);
        System.out.println("DNA Recorded to "+fileOutputName_);
        dnaWriter.close();
    }

    public void FileSend(String dnaToWrite_) throws IOException
    {
        Scanner outputLocationReader = new Scanner(System.in);
        System.out.println("Please input the name of the file you'd like to save your DNA results to: ");
        String outputLocation = outputLocationReader.nextLine();
        BufferedWriter dnaWriter = new BufferedWriter(new FileWriter(outputLocation));
        dnaWriter.write(dnaToWrite_);
        System.out.println("DNA Recorded to "+outputLocation);
        dnaWriter.close();
        outputLocationReader.close();

    }
}
