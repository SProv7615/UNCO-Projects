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
public class AnalysisEngineTester
{
    public static void main(String args[]) {

        AnalysisEngine aeTest1 = new AnalysisEngine("Testing","testing","Testing","AERepository.txt","AEDepository.txt");

        aeTest1.Phase1();
        aeTest1.Phase2();
        aeTest1.Phase3();

        AnalysisEngine aeTest2 = new AnalysisEngine("DefaultRepository.txt","DefaultDepository.txt");

        aeTest2.Phase1();
        aeTest2.Phase2();
        aeTest2.Phase3();

        AnalysisEngine aeTest3 = new AnalysisEngine();
        aeTest3.Phase1();
        aeTest3.Phase2();
        aeTest3.Phase3();
    }
}
