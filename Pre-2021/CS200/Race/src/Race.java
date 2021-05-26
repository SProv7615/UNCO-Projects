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
 * Did someone say Race War? Well, there's a race, and there might be a war, but*
 * there is not, strictly speaking, a race war.                                 *
 * COPYRIGHT:                                                                   *
 * This program is (c) 2019 Stephen Provost.                                    *
 * This is original work, without use of outside sources.                       *
 *******************************************************************************/

import java.util.*;
public class Race {
    private String strEvent;
    private String strDisplay, strTime;
    private int intRaceLength = 1000;
    private ArrayList<Animal> aniContestants = new ArrayList<Animal>();
    public Race(String strEvent_,int intRaceLength_, ArrayList<Animal> aniContestants_)
    {
        this.strEvent = strEvent_;
        this.intRaceLength = intRaceLength_;
        this.aniContestants = aniContestants_;
    }

    public Race(int RaceLength_, ArrayList<Animal> aniContestants_)
    {
        strEvent = "The Mutha-F****ing Race of the Century!";
        this.intRaceLength = RaceLength_;
        this.aniContestants = aniContestants_;
    }

    public Race(ArrayList<Animal> aniContestants_)
    {
        strEvent = "The Generic Race";
        this.intRaceLength = 1000;
        this.aniContestants = aniContestants_;
    }

    //The grand enchilada: calls the update time for each contestant and makes sure they display properly.
    public void runRace()
    {
        raceStart();
        raceFormat();
        double max = 0;
        for(double i = 0; i <= intRaceLength; i--)
        {
            strTime = String.format("| %4d |",aniContestants.get(0).getTime());
            System.out.print(strTime);
            for(Animal ani : aniContestants)
            {
                ani.updatePosition();
                if(ani.getCurrentPosition() > max)
                {
                    max = ani.getCurrentPosition(); //Polymorphism is present here: each getCurrentPosition calls a
                                                    // special prompt from the non-Animal classes.
                    i = max;
                }
            }
            System.out.println();
        }
        strTime = String.format("| %4d |",aniContestants.get(0).getTime());
        System.out.print(strTime);
        for(Animal ani : aniContestants)
        {
            ani.updatePosition();
        }

        System.out.println();
        topLine();
        raceEnd();
    }

    private void topLine()
    {
        String aniSpecies = "";
        System.out.print("+------+");
        for(Animal a : aniContestants)
        {
            if(a.getSpecies() != "Hare" && a.getSpecies() != "Dog" && a.getSpecies() != "Phase Beast")
            {
                System.out.print("-----------------+");
            }
            else
            {
                System.out.print("----------------------------+");
            }
        }
        System.out.println();
    }

    private void secondLine()
    {
        String aniName = "";
        System.out.print("|      |");
        for(Animal a : aniContestants)
        {
            aniName = a.getName();
            if(a.getSpecies() != "Hare" && a.getSpecies() != "Dog" && a.getSpecies() != "Phase Beast")
            {
                strDisplay = String.format("%11s      |",aniName);
            }
            else
            {
                strDisplay = String.format("   %15s          |",aniName);
            }
            System.out.print(strDisplay);
        }
        System.out.println();
    }

    private void thirdLine()
    {
        String aniSpecies = "";
        System.out.print("|      |");
        for(Animal a : aniContestants)
        {
            if(a.getSpecies() != "Hare" && a.getSpecies() != "Dog" && a.getSpecies() != "Phase Beast")
            {
                strDisplay = String.format("  %11s    |","("+a.getSpecies()+")");
            }
            else
            {
                strDisplay = String.format("   %15s          |","("+a.getSpecies()+")");
            }
            System.out.print(strDisplay);
        }
        System.out.println();
    }

    private void fourthLine()
    {
        String aniSpecies = "";
        System.out.print("| Time |");
        for(Animal a : aniContestants)
        {
            if(a.getSpecies() != "Hare" && a.getSpecies() != "Dog" && a.getSpecies() != "Phase Beast")
            {
                strDisplay = (" Position Speed  |");
            }
            else
            {
                strDisplay = ("   Position Speed Comments  |");
            }
            System.out.print(strDisplay);
        }
        System.out.println();
    }

    //The top formatting for the grid.
    private void raceFormat()
    {
        topLine();
        secondLine();
        thirdLine();
        fourthLine();
    }

    //The ending; due to the way that my time was kept, I had to subtract 1 from the time to display properly.
    private void raceEnd()
    {
        Double max = 0.0;
        String winner = "";
        System.out.println();
        System.out.println("Race over in "+(aniContestants.get(0).getTime()-1)+" seconds!");
        for(Animal ani : aniContestants)
        {
            if(max < ani.getCurrentPosition())
            {
                max = ani.getCurrentPosition();
                winner = ani.getSpecies();
            }
        }
        System.out.println(winner+" wins!!!");
        System.out.println();
    }

    //The beginning of the race: displays the event, distance, and the contestants.
    private void raceStart()
    {
        int counter = 1;
        System.out.println("Event: "+strEvent);
        System.out.println();
        System.out.println("Race Distance (feet): "+intRaceLength);
        System.out.println();
        for(Animal ani : aniContestants)
        {
            System.out.println("Contestant "+counter+": " + ani.getName() + " The " + ani.getSpecies());
            ani.aniIntro(); // Polymorphism:Each animal type has it's own intro due to special 'abilities' that
                            // may be implemented during the race.
            counter++;
        }
        System.out.println();
        System.out.println("-----------------------------------------------------------------------------------------");
        System.out.println("Aaaaaaaaaaaand we're OFF!!!");
        System.out.println();
    }
}