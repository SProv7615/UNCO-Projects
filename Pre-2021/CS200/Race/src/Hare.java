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
 * A hare is not a hair, but is perhaps covered by hair.                        *
 *                                                                              *
 * COPYRIGHT:                                                                   *
 * This program is (c) 2019 Stephen Provost.                                    *
 * This is original work, without use of outside sources.                       *
 *******************************************************************************/

public class Hare extends Animal
{
    private int intStartNapTime, intNapDuration, intTimeSpentSleeping;
    private Boolean booNapping;
    public Hare(String strName_,double douRunningSpeed_,double douVariationofSpeed_,
                double douCurrentPosition_, int intStartNapTime_, int intNapDuration_)
    {
        super(strName_,"Hare", douRunningSpeed_,douVariationofSpeed_,douCurrentPosition_);
        this.intStartNapTime = intStartNapTime_;
        this.intNapDuration = intNapDuration_;
        this.booNapping = false;
    }

    public Hare()
    {
        this("Reg",20,12,0,30,30);
    }

    public int getStartNapTime()
    {
        return(intStartNapTime);
    }

    public int getIntNapDuration()
    {
        return(intNapDuration);
    }

    public Boolean getbooNapping()
    {
        return(booNapping);
    }

    public Boolean napBegin()
    {
        booNapping = true;
        return booNapping;
    }

    public Boolean napEnds()
    {
        booNapping = false;
        return booNapping;
    }

    public double updatePosition()
    {
        if(intCurTime == intStartNapTime)
        {
            napBegin();
        }
        else if(intCurTime == intStartNapTime+intNapDuration)
        {
            napEnds();
        }
        if(booNapping == true)
        {
            douCurrentVariation = 0.0;
            intTimeSpentSleeping++;
        }
        else if(booNapping == false)
        {
            int CoinToss = douRandomRun.nextInt(2);
            Double douRunVari = douRandomRun.nextDouble();
            if (CoinToss == 0) {
                douCurrentVariation = douRunningSpeed - (douVariationofSpeed * douRunVari);
            } else {
                douCurrentVariation = douRunningSpeed + (douVariationofSpeed * douRunVari);
            }
        }
        outputDisplay();
        updateTime();
        douCurrentPosition+=douCurrentVariation;
        return douCurrentPosition;
    }

    public void outputDisplay()
    {
        String strDisplay = "";
        if(booNapping==true)
        {
            strDisplay = String.format(" %8s  %5s  %4s%-4d  |",formatting(douCurrentPosition),formatting(douCurrentVariation),"Nap-",intTimeSpentSleeping);
        }
        else
        {
            strDisplay = String.format(" %8s  %5s  %8s  |",formatting(douCurrentPosition),formatting(douCurrentVariation),""); //28
        }
        System.out.print(strDisplay);
    }

    public void aniIntro()
    {
        System.out.println("    Running Speed: " + this.getRunSpeed());
        System.out.println("    Variation of Speed: " + this.getRunSpeedVari());
        System.out.println("    Nap Trap: "+this.getStartNapTime());
        System.out.println("    Nap Duration: "+this.getIntNapDuration());
        System.out.println();
    }
}
