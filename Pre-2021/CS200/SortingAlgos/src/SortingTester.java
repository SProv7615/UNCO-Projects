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
 *******************************************************************************/public class SortingTester
{
    public static void main(String args[]) {
        Sorting sorListTester = new Sorting();
        sorListTester.addInt(3);
        sorListTester.addInt(1);
        sorListTester.addInt(4);
        sorListTester.addInt(1);
        sorListTester.addInt(5);
        sorListTester.addInt(9);
        sorListTester.addInt(2);
        sorListTester.addInt(6);
        sorListTester.bubbleSort();

        sorListTester.setNumofNums(10);
        sorListTester.setLowofLows(0);
        sorListTester.setHighofHighs(99);
        sorListTester.randomAddInt();
        sorListTester.bubbleSort();

        //Insertion Sort
        sorListTester.addInt(3);
        sorListTester.addInt(1);
        sorListTester.addInt(4);
        sorListTester.addInt(1);
        sorListTester.addInt(5);
        sorListTester.addInt(9);
        sorListTester.addInt(2);
        sorListTester.addInt(6);
        sorListTester.insertionSort();

        sorListTester.setNumofNums(10);
        sorListTester.setLowofLows(0);
        sorListTester.setHighofHighs(99);
        sorListTester.randomAddInt();
        sorListTester.insertionSort();

        //Selection Sort
        sorListTester.addInt(3);
        sorListTester.addInt(1);
        sorListTester.addInt(4);
        sorListTester.addInt(1);
        sorListTester.addInt(5);
        sorListTester.addInt(9);
        sorListTester.addInt(2);
        sorListTester.addInt(6);
        sorListTester.printList();
        sorListTester.selectionSort();

        sorListTester.printList();
        sorListTester.setNumofNums(10);
        sorListTester.setLowofLows(0);
        sorListTester.setHighofHighs(99);
        sorListTester.randomAddInt();
        sorListTester.selectionSort();

        //sorListTester.runQuickSorter();
    }

}
