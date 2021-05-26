/*******************************************************************************
 *                           Assignment 2                                       *
 *                                                                              *
 * PROGRAMMER:       Stephen Provost                                            *
 * CLASS:            CS200                                                      *
 * ASSIGNMENT:       Assignment assig-2                                         *
 * INSTRUCTOR:       Dean Zeller                                                *
 * SUBMISSION DATE:  10/2/2019                                                  *
 *                                                                              *
 * DESCRIPTION:                                                                 *
 * Incomplete algorithms to sort data.                                          *
 *                                                                              *
 * COPYRIGHT:                                                                   *
 * This program is (c) 2019 Stephen Provost.                                    *
 * This is original work, without use of outside sources.                       *
 *******************************************************************************/
import java.util.*;

public class Sorting
{
    private ArrayList<Integer> SortingList = new ArrayList<Integer>();
    private int intAdder = 0;
    private int intNumofNums = 0;
    private int intLowofLows = 0;
    private int intHighofHighs = 0;
    boolean booSorted = false;

    public int setNumofNums(int intNumofNums_)
    {
        this.intNumofNums = intNumofNums_;
        return intNumofNums;
    }

    public int setLowofLows(int intLowofLows_)
    {
        this.intLowofLows = intLowofLows_;
        return intLowofLows;
    }

    public int setHighofHighs(int intHighofHighs_)
    {
        this.intHighofHighs = intHighofHighs_;
        return intHighofHighs;
    }

    public void addInt(int intAdder_)
    {
        this.intAdder = intAdder_;
        this.SortingList.add(intAdder);
    }

    public ArrayList<Integer> randomAddInt()
    {
        for(int i = 0; i < intNumofNums; i++)
        {
            Random ranNum = new Random();
            int randNum = (ranNum.nextInt(intHighofHighs-intLowofLows) + intLowofLows);
            SortingList.add(randNum);
        }
        return SortingList;
    }

    public void clearList()
    {
        SortingList.clear();
    }

    public void printList()
    {
        for(int i = 0; i < SortingList.size(); i++)
        {
            System.out.print(SortingList.get(i)+"  ");
        }
    }

    public void bubbleSort()
    {
        int intBubbleSwap = 0;
        int intBubbleCompare = 1;
        int intLoopCounter = 1;
        System.out.println("#####################################################################");
        System.out.println("Bubble Sort");
        System.out.println("#####################################################################");
        while(booSorted == false)
        {
            booSorted= true;
            System.out.print("Loop #"+intLoopCounter+":    Array = ");
            for(int intLoopNum = 0; intLoopNum < SortingList.size(); intLoopNum++)
            {
                System.out.print(SortingList.get(intLoopNum));
                System.out.print("  ");
            }
            System.out.println();
            intLoopCounter++;
            for(int i = 0; i < SortingList.size() - 1; i++)
            {
                System.out.print("   Comparison #"+intBubbleCompare + " ");
                for(int intSpaceCounter = i+1; intSpaceCounter > 0; intSpaceCounter--)
                {
                    System.out.print("   ");
                }
                System.out.print(SortingList.get(i) + "  " +SortingList.get(i+1));
                System.out.println();
                intBubbleCompare++;
                if(SortingList.get(i) > SortingList.get(i+1))
                {
                    int intTemp = SortingList.get(i+1);
                    SortingList.set(i+1,SortingList.get(i));
                    SortingList.set(i,intTemp);
                    booSorted=false;
                    intBubbleSwap++;
                    System.out.print("   Swap #"+intBubbleSwap+":         ");
                    for(int spaces = i; spaces > 0; spaces--)
                    {
                        System.out.print("   ");
                    }
                    System.out.print(SortingList.get(i) + "  " + SortingList.get(i+1));
                    System.out.println();
                }

            }
        }
        printList();
        System.out.println();
        System.out.println("Analysis:");
        System.out.println("\tComparisons: \t"+intBubbleCompare);
        System.out.println("\tSwaps: \t"+intBubbleSwap);
        System.out.println("\tWork: \t"+intBubbleCompare +" + "+intBubbleSwap + "*8 = "+ (intBubbleCompare + intBubbleSwap*8));
        clearList();
        booSorted=false;
    }

    public void insertionSort()
    {
        int intSwapCounter = 0;
        int intCompCounter = 1;
        int intLoopNum = 1;
        System.out.println("#####################################################################");
        System.out.println("Insertion Sort");
        System.out.println("#####################################################################");
            for (int j = 1; j < SortingList.size(); j++)
            {
                System.out.print("Loop #" + intLoopNum + ":    Array = ");
                printList();
                System.out.println();
                int k = j;
                System.out.print("   Comparison #"+intCompCounter + "");
                boolean firstComp = false;
                do {
                    int intSpaceCounter = j;
                    for(int spaces = intSpaceCounter; spaces > 0; spaces--)
                    {
                        System.out.print("    ");
                    }
                    System.out.print(SortingList.get(k-1) + "  "+SortingList.get(k) +"\n");
                    intCompCounter++;
                    if(SortingList.get(k-1) > SortingList.get(k))
                    {
                        if(firstComp==false) {
                            int intSmallerIndexNum = k - 1;
                            int intTempGreater = SortingList.get(intSmallerIndexNum);
                            int intTempLesser = SortingList.get(k);
                            SortingList.set(intSmallerIndexNum, intTempLesser);
                            SortingList.set(k, intTempGreater);
                            intSwapCounter++;
                            firstComp = true;
                        }
                        else
                        {
                            System.out.print("   Comparison #"+intCompCounter + " ");
                            for(int spaces = intSpaceCounter; spaces > 0; spaces--)
                            {
                                System.out.print("    ");
                            }
                            System.out.print(SortingList.get(k-1) + "  "+SortingList.get(k) +"\n");
                            intCompCounter++;
                            intSwapCounter++;
                            intSpaceCounter--;
                            int intSmallerIndexNum = k - 1;
                            int intTempGreater = SortingList.get(intSmallerIndexNum);
                            int intTempLesser = SortingList.get(k);
                            SortingList.set(intSmallerIndexNum, intTempLesser);
                            SortingList.set(k, intTempGreater);

                        }
                }
                    k--;
                } while(k > 0 && SortingList.get(k-1) > SortingList.get(k));
                intLoopNum++;
            }
            printList();
            System.out.println();
        System.out.println("Analysis:");
        System.out.println("\tComparisons: \t"+intCompCounter);
        System.out.println("\tSwaps: \t"+intSwapCounter);
        System.out.println("\tWork: \t"+intCompCounter +" + "+intSwapCounter + "*8 = "+ (intCompCounter + intSwapCounter*8));
        SortingList.clear();
    }


    public void selectionSort()
    {
        int intSwap = 0;
        int intComparison = 0;
        for(int i = 0; i < SortingList.size(); i++)
        {
            int intMin = SortingList.get(i);
            int intMinID = i;
            for (int intExplore = i+1; intExplore < SortingList.size(); intExplore++)
            {
                intComparison++;
                if(SortingList.get(intExplore) < intMin)
                {
                    intMin = SortingList.get(intExplore);
                    intMinID = intExplore;
                    intSwap++;
                }
            }
            int intTempID = SortingList.get(i);
            SortingList.set(i,intMin);
            SortingList.set(intMinID,intTempID);
        }
        printList();
        System.out.println();
        System.out.println("Analysis:");
        System.out.println("\tComparisons: \t"+intComparison);
        System.out.println("\tSwaps: \t"+intSwap);
        System.out.println("\tWork: \t"+intComparison +" + "+intSwap + "*8 = "+ (intComparison + intSwap*8));
        SortingList.clear();
    }

    public void quickSort(int low, int high)
    {
        if(low < high)
        {
            System.out.println("Level ");
            //this.levelnum++
            int p = partition(low,high);
            this.quickSort(low,p-1);
            this.quickSort(p+1,high);

            printList();
        }
    }

    public int partition(int low, int high)
    {
        int intPivot = SortingList.get(high);
        int i = low;
        System.out.println("\tLow = " +low + "\n\tHigh = "+high+ "\n\tPivot = " +intPivot);
        for(int j = low; j <= high-1; j++)
        {
            if(SortingList.get(j) < intPivot)
            {
                int intHigherVal = SortingList.get(i);
                int intLowerVal = SortingList.get(j);
                SortingList.set(i,intLowerVal);
                SortingList.set(j,intHigherVal);
                //set SortingList(i to j)
            }
            i++;
        }
        if(SortingList.get(i) != SortingList.get(high))
        {
            int intNewiVal = SortingList.get(high);
            int intNewHighVal = SortingList.get(i);
            SortingList.set(i,intNewiVal);
            SortingList.set(high,intNewHighVal);
            //Make Swap (i, high)
        }
        return(i);
    }


    public void runQuickSorter()
    {
        this.quickSort(0,SortingList.size()-1);
    }


}
