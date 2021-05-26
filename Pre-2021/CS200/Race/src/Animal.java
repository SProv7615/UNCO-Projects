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
 * The basest of animals, with no special features. How droll.                  *
 *                                                                              *
 * COPYRIGHT:                                                                   *
 * This program is (c) 2019 Stephen Provost.                                    *
 * This is original work, without use of outside sources.                       *
 *******************************************************************************/

import java.util.*;
import java.text.DecimalFormat;

public class Animal
{
    protected String strName, strSpecies;
    protected double douRunningSpeed, douVariationofSpeed, douCurrentPosition;
    protected int intCurTime;
    protected Random douRandomRun = new Random();
    protected DecimalFormat myFormatter = new DecimalFormat("###.#");
    protected double douCurrentVariation = 0.0;
    protected int randomInt;

    public Animal(String strName_,String strSpecies_,double douRunningSpeed_,double douVariationofSpeed_,
                  double douCurrentPosition_)
    {
        this.strName = strName_;
        this.strSpecies = strSpecies_;
        this.douRunningSpeed = douRunningSpeed_;
        this.douVariationofSpeed = douVariationofSpeed_;
        this.douCurrentPosition = douCurrentPosition_;
        this.intCurTime = 0;
    }

    public Animal(String strName_,String strSpecies_,double douRunningSpeed_,double douVariationofSpeed_)
    {
        this(strName_,strSpecies_,douRunningSpeed_,douVariationofSpeed_,0);
    }

    public Animal(String strName_,String strSpecies_,double douRunningSpeed_)
    {
        this(strName_,strSpecies_,douRunningSpeed_,douRunningSpeed_*.1,0);
    }

    public Animal(String strName_,double douRunningSpeed_,double douVariationofSpeed_,
                  double douCurrentPosition_)
    {
        this("Beast", "Animal",douRunningSpeed_,douRunningSpeed_*.1,douCurrentPosition_);
    }

    public Animal()
    {
        this("Beast","Disney Creature",10,10*.1,0);
    }

    public String getName()
    {
        return strName;
    }

    public String getSpecies()
    {
        return strSpecies;
    }

    public double getRunSpeed()
    {
        return douRunningSpeed;
    }

    public double setRunSpeed(double douRunSpeed_)
    {
        this.douRunningSpeed = douRunSpeed_;
        return douRunningSpeed;
    }

    public double getRunSpeedVari()
    {
        return douVariationofSpeed;
    }

    public double setRunSpeedVari(double douVariationofSpeed_)
    {
        this.douVariationofSpeed=douVariationofSpeed_;
        return douVariationofSpeed;
    }

    public double getCurrentPosition()
    {
        return douCurrentPosition;
    }

    public double setCurrentPosition(double douCurrentPosition_)
    {
        this.douCurrentPosition=douCurrentPosition_;
        return douCurrentPosition;
    }

    public int getTime()
    {
        return intCurTime;
    }

    public int updateTime()
    {
        intCurTime++;
        return intCurTime;
    }

    public String formatting(double ToFormat)
    {
        String strFormatted = myFormatter.format(ToFormat);
        return strFormatted;
    }

    public double updatePosition()
    {
        int CoinToss = douRandomRun.nextInt(2);
        Double douRunVari = douRandomRun.nextDouble();
        if(CoinToss == 0)
        {
            douCurrentVariation = douRunningSpeed - (douVariationofSpeed*douRunVari);
        }
        else
        {
            douCurrentVariation = douRunningSpeed + (douVariationofSpeed*douRunVari);
        }
        outputDisplay();
        updateTime();
        douCurrentPosition+=douCurrentVariation;
        return douCurrentPosition;
    }

    public void outputDisplay()
    {
        String strDisplay = String.format(" %8s  %5s |",formatting(douCurrentPosition),formatting(douCurrentVariation)); //17
        System.out.print(strDisplay);
    }

    public void aniIntro()
    {
        System.out.println("    Running Speed: " + this.getRunSpeed());
        System.out.println("    Variation of Speed: " + this.getRunSpeedVari());
        System.out.println();
    }

    public int randomize(int randomBound)
    {
        this.randomInt = douRandomRun.nextInt(randomBound);
        return this.randomInt;
    }

    public int getRandom()
    {
        return this.randomInt;
    }
}
