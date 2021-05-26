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

package bioinformatics;
import input.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class toolkit
{
    String chara, rawData, erroredData, cleanData, dataRNA, mostCommonSeqString, moddedCleanData, replacedCleanData;
    Integer count, foundVal, subsequenceSearch;
    int firstSeqLoc = -1, maxHash;
    HashMap<String,Integer> badDNAHashCounter = new HashMap<>();
    HashMap<String,Integer> singlesHash = new HashMap<>();
    HashMap<String,Integer> doublesHash = new HashMap<>();
    HashMap<String,Integer> triplesHash = new HashMap<>();
    HashMap<String,Integer> mostCommonSequenceHash = new HashMap<>();
    StringBuilder displayErrorBuilder = new StringBuilder();
    ArrayList<Integer> aListofLocations = new ArrayList<>();

    public String displayErrors(String rawData_)
    {
        this.rawData = rawData_.toUpperCase();
        for(int i = 0; i < this.rawData.length(); i++)
        {
            if(this.rawData.charAt(i)!=('A') && this.rawData.charAt(i)!=('C') && this.rawData.charAt(i)!=('G') && this.rawData.charAt(i)!=('T'))
            {
                this.displayErrorBuilder.append(this.rawData.charAt(i));
                if(!this.badDNAHashCounter.containsKey(Character.toString(this.rawData.charAt(i))))
                {
                    this.badDNAHashCounter.put(Character.toString(this.rawData.charAt(i)),1);
                }
                else
                {
                    this.badDNAHashCounter.put(Character.toString(this.rawData.charAt(i)),this.badDNAHashCounter.get(Character.toString(this.rawData.charAt(i)))+1);
                }
            }
            else
            {
                char toLower = this.rawData.charAt(i);
                toLower+=32;
                this.displayErrorBuilder.append(toLower);
            }
        }
        return this.rawData;
    }

    public String cleanErrors()
    {
        String cleanErrorData = this.rawData.toUpperCase();
        StringBuilder cleanErrorBuilder = new StringBuilder();
        for(int i = 0; i < cleanErrorData.length(); i++) {
            if (cleanErrorData.charAt(i) == ('A') || cleanErrorData.charAt(i) == ('C') || cleanErrorData.charAt(i) == ('G') || cleanErrorData.charAt(i) == ('T'))
            {
                cleanErrorBuilder.append(cleanErrorData.charAt(i));
            }
        }
        return this.cleanData = cleanErrorBuilder.toString();
    }

    public String generateRNA()
    {
        StringBuilder rnaBuilder = new StringBuilder();
        for(int i = 0; i < cleanData.length(); i++)
        {
            if (cleanData.charAt(i) == ('T'))
            {
                rnaBuilder.append('U');
            }
            else
            {
                rnaBuilder.append(cleanData.charAt(i));
            }
        }
        dataRNA = rnaBuilder.toString();
        return dataRNA;
    }

    public int searchSingleSequence(String searchSeq_)
    {
        Boolean found = false;
        for(int i = 0; i < cleanData.length()+1-searchSeq_.length(); i++)
        {
            if(cleanData.charAt(i) == searchSeq_.charAt(0) && !found)
            {
                for(int j = 0; j < searchSeq_.length(); j++)
                {
                    if(cleanData.charAt(i+j)==searchSeq_.charAt(j))
                    {
                        found = true;
                        firstSeqLoc = i;
                    }
                    else
                    {
                        found = false;
                        firstSeqLoc = -1;
                        break;
                    }
                }
            }
        }
        return firstSeqLoc;
    }

    public ArrayList<Integer> searchMultiSequence(String searchSeq_)
    {
        int seqLoc = 0;
        Boolean found = false;
        Boolean last = false;
        for(int i = 0; i < cleanData.length()-(searchSeq_.length()-1); i++)
        {
            if(cleanData.charAt(i) == searchSeq_.charAt(0))
            {
                seqLoc = i;
                for(int j = 0; j < searchSeq_.length(); j++)
                {
                    if(cleanData.charAt(i+j)==searchSeq_.charAt(j))
                    {
                        found = true;
                    }
                    else
                    {
                        found = false;
                        last = false;
                        break;
                    }
                    if(cleanData.charAt(i+searchSeq_.length()-1)==searchSeq_.charAt(searchSeq_.length()-1) && !last)
                    {
                        last = true;
                    }
                }
                if(found && last)
                {
                    this.aListofLocations.add(seqLoc);
                    found = false;
                    last = false;
                }
            }
        }
        return this.aListofLocations;
    }

    public HashMap<String,Integer> simpleSingleAnalysis()
    {
        String tempString;
        char tempChar;
        for(int i = 0; i < this.cleanData.length();i++)
        {
            tempChar = this.cleanData.charAt(i);
            tempString = Character.toString(tempChar);
            if(!this.singlesHash.containsKey(tempString))
            {
                this.singlesHash.put(tempString,1);
            }
            else
            {
                this.singlesHash.put(tempString,this.singlesHash.get(tempString)+1);
            }
        }
        return singlesHash;
    }

    public HashMap<String,Integer> simpleDoubleAnalysis()
    {
        String tempString;
        for(int i = 2; i <= this.cleanData.length();i++)
        {
            tempString = this.cleanData.substring(i-2,i);
            if(!this.doublesHash.containsKey(tempString))
            {
                this.doublesHash.put(tempString,1);
            }
            else
            {
                this.doublesHash.put(tempString,this.doublesHash.get(tempString)+1);
            }
        }
        return doublesHash;
    }

    public HashMap<String,Integer> simpleTripleAnaylsis()
    {
        String tempString;
        for(int i = 3; i <= this.cleanData.length();i++)
        {
            tempString = this.cleanData.substring(i-3,i);
            if(!this.triplesHash.containsKey(tempString))
            {
                this.triplesHash.put(tempString,1);
            }
            else
            {
                this.triplesHash.put(tempString,this.triplesHash.get(tempString)+1);
            }
        }
        return triplesHash;
    }

    public void simpleAnalysis()
    {
        simpleSingleAnalysis();
        simpleDoubleAnalysis();
        simpleTripleAnaylsis();
    }

    public String mostCommonSequence(int desiredLength)
    {
        String tempString;
        this.maxHash = 0;
        for(int i = desiredLength; i <= this.cleanData.length();i++)
        {
            tempString = this.cleanData.substring(i-desiredLength,i);
            if(!this.mostCommonSequenceHash.containsKey(tempString))
            {
                this.mostCommonSequenceHash.put(tempString,1);
                this.maxHash = 1;
            }
            else
            {
                this.mostCommonSequenceHash.put(tempString,this.mostCommonSequenceHash.get(tempString)+1);
                if(this.mostCommonSequenceHash.get(tempString)>maxHash)
                {
                    this.maxHash = this.mostCommonSequenceHash.get(tempString);
                    this.mostCommonSeqString = tempString;
                }
            }
        }
        if(this.maxHash == 0)
        {
            this.maxHash = -1;
        }
        return this.mostCommonSeqString;
    }

    public Integer searchSubsequence(String subsequenceToBeSearchedFor)
    {
        int searchNum = 0;
        Boolean search = false;
        for(int i = 0; i<cleanData.length();i++)
        {
            if(cleanData.charAt(i)==subsequenceToBeSearchedFor.charAt(0) && searchNum == 0)
            {
                searchNum++;
                this.subsequenceSearch=i;
            }
            else if(cleanData.charAt(i)==subsequenceToBeSearchedFor.charAt(searchNum) && !search)
            {
                searchNum++;
            }
            if(searchNum == subsequenceToBeSearchedFor.length()-1)
            {
                search=true;
            }
        }
        if(search)
        {
            return this.subsequenceSearch;
        }
        else
        {
            return this.subsequenceSearch=-1;
        }
    }

    public String removeSequence(String removeSequence)
    {
        StringBuilder newCleanDataBuilder = new StringBuilder();
        Boolean found = false;
        int seqRemove = 0;
        for(int i = 0; i < cleanData.length()-(removeSequence.length()-1); i++)
        {
            if(cleanData.charAt(i)==removeSequence.charAt(0) && !found)
            {
                for(int j = 0; j < removeSequence.length()-1;j++)
                {
                    if(cleanData.charAt(i+j)==removeSequence.charAt(j)) {
                        found=true;
                        seqRemove = i;
                    }
                    else
                    {
                        found=false;
                        seqRemove=(-1);
                    }
                }

            }
        }
        if(found)
        {
            for (int i = 0; i < cleanData.length(); i++) {
                if(i!=seqRemove)
                {
                    newCleanDataBuilder.append(cleanData.charAt(i));
                }
                else
                {
                    i+=(removeSequence.length()-1);
                }
            }
            foundVal(1);
            return this.moddedCleanData = newCleanDataBuilder.toString();
        }
        else
        {
            foundVal(-1);
            return cleanData;
        }
    }

    public String replaceSequence(String replaceSequence, String newSequence)
    {
        StringBuilder newCleanDataBuilder = new StringBuilder();
        Boolean found = false;
        int seqRemove = 0;
        for(int i = 0; i < cleanData.length()-(replaceSequence.length()-1); i++)
        {
            if(cleanData.charAt(i)==replaceSequence.charAt(0) && !found)
            {
                for(int j = 0; j < replaceSequence.length()-1;j++)
                {
                    if(cleanData.charAt(i+j)==replaceSequence.charAt(j)) {
                        found=true;
                        seqRemove = i;
                    }
                    else
                    {
                        found=false;
                        seqRemove=(-1);
                    }
                }

            }
        }
        if(found)
        {
            for (int i = 0; i < cleanData.length(); i++) {
                if(i!=seqRemove)
                {
                    newCleanDataBuilder.append(cleanData.charAt(i));
                }
                else
                {
                    for(int j = 0; j < newSequence.length(); j++)
                    {
                        newCleanDataBuilder.append(newSequence.charAt(j));
                    }
                    i+=(replaceSequence.length()-1);
                }
            }
            foundVal(1);
            return this.replacedCleanData = newCleanDataBuilder.toString();
        }
        else
        {
            foundVal(-1);
            return cleanData;
        }
    }


    public void toolkitReport() throws IOException
    {
        FileInput analysisReporter = new FileInput();
        System.out.println("____________________________________________________________________________________________");
        System.out.println("|_______________________________DNA Analysis Report_________________________________________|");
        System.out.println("|Raw Data: "+rawData);
        System.out.println("|Clean Data: "+cleanData);
        System.out.println("|Generate RNA: "+dataRNA);
        System.out.println("|Found First Sequence: "+firstSeqLoc);
        System.out.println("|Found Multi Sequence: "+aListofLocations.toString());
        System.out.println("|Found Simple Single Analysis: "+singlesHash.toString());
        System.out.println("|Found Simple Double Analysis: "+doublesHash.toString());
        System.out.println("|Found Simple Triple Analysis: "+triplesHash.toString());
        System.out.println("|Found Most Common Sequence: "+mostCommonSeqString+" Found: "+maxHash+" Times");
        System.out.println("|Subsequence Found at: "+subsequenceSearch);
        System.out.println("|Removed Sequence: "+foundVal);
        System.out.println("|New Clean Data: "+moddedCleanData);
        System.out.println("|New Replaced Data: "+replacedCleanData);
        System.out.println("____________________________________________________________________________________________");
        analysisReporter.FileSend("Report.txt",rawData,cleanData,dataRNA);
    }

    public int foundVal(int val)
    {
        this.foundVal = val;
        return this.foundVal;
    }

}
