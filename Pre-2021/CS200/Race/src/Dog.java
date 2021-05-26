/*******************************************************************************
 *                           Assignment 3                                       *
 *                                                                              *
 * PROGRAMMER:       Stephen Provost                                            *
 * CLASS:            CS200                                                      *
 * ASSIGNMENT:       Assignment assig-3                                         *
 * INSTRUCTOR:       Dean Zeller                                                *
 * SUBMISSION DATE:  11/1/2019                                                  *
 *                                                                              *
 * DESCRIPTION:                                                                 *
 * A dog is man's best friend... unless there's a squirrel.                     *
 *                                                                              *
 * COPYRIGHT:                                                                   *
 * This program is (c) 2019 Stephen Provost.                                    *
 * This is original work, without use of outside sources.                       *
 *******************************************************************************/

public class Dog extends Animal
{
    private int intSquirrelRun, intSquirrelTracker = 0;
    private Boolean booSquirrel, booSquirrelTracker;
    public Dog(String strName_,double douRunningSpeed_,double douVariationofSpeed_,
                double douCurrentPosition_,int intSquirrelRun_)
    {
        super(strName_,"Dog", douRunningSpeed_,douVariationofSpeed_,douCurrentPosition_);
        this.intSquirrelRun = intSquirrelRun_;
        this.booSquirrel = false;
        this.booSquirrelTracker=false;
    }

    public Dog()
    {
        this("Doug",16,16*.1,0, 100);
    }

    public int getIntSquirrelRun()
    {
        return(intSquirrelRun);
    }

    public boolean booSquirrel()
    {
        return(booSquirrel);
    }

    public double updatePosition()
    {
        int CoinToss = douRandomRun.nextInt(2);
        Double douRunVari = douRandomRun.nextDouble();
        int ForwardorBack = douRandomRun.nextInt(2);
        if(douCurrentPosition>=intSquirrelRun && booSquirrelTracker == false)
        {
            booSquirrelTracker = true;
            booSquirrel = true;
        }
        if(intSquirrelTracker >= intSquirrelRun)
        {
            booSquirrel=false;
        }
        if(booSquirrel == true && ForwardorBack == 0)
        {
            if (CoinToss == 0) {
                douCurrentVariation = -1*(douRunningSpeed - (douVariationofSpeed * douRunVari));
            } else {
                douCurrentVariation = -1*(douRunningSpeed + (douVariationofSpeed * douRunVari));
            }
            intSquirrelTracker++;
        }
        else if(booSquirrel == true && ForwardorBack == 1)
        {
            if (CoinToss == 0) {
                douCurrentVariation = 1*(douRunningSpeed - (douVariationofSpeed * douRunVari));
            } else {
                douCurrentVariation = 1*(douRunningSpeed + (douVariationofSpeed * douRunVari));
            }
            intSquirrelTracker++;
        }
        else {
            if (CoinToss == 0) {
                douCurrentVariation = douRunningSpeed - (douVariationofSpeed * douRunVari);
            } else {
                douCurrentVariation = douRunningSpeed + (douVariationofSpeed * douRunVari);
            }
        }
        updateTime();
        outputDisplay();
        douCurrentPosition+=douCurrentVariation;
        return douCurrentPosition;
    }

    public void outputDisplay()
    {
        String strDisplay = "";
        if(booSquirrel==true)
        {
            strDisplay = String.format(" %8s  %5s  %8s  |",formatting(douCurrentPosition),formatting(douCurrentVariation),"Squirrel");
        }
        else
        {
            strDisplay = String.format(" %8s  %5s  %8s  |",formatting(douCurrentPosition),formatting(douCurrentVariation),"");
        }
        System.out.print(strDisplay);
    }

    public void aniIntro()
    {
        System.out.println("    Running Speed: " + this.getRunSpeed());
        System.out.println("    Variation of Speed: " + this.getRunSpeedVari());
        System.out.println("    Squirrel Trap: "+this.getIntSquirrelRun());
        System.out.println();
    }

}
