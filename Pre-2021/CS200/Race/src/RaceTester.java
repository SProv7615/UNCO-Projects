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
 * A tester for the races and the animals that go in them. Humanity not allowed.*
 *                                                                              *
 * COPYRIGHT:                                                                   *
 * This program is (c) 2019 Stephen Provost.                                    *
 * This is original work, without use of outside sources.                       *
 *******************************************************************************/

import java.util.*;

public class RaceTester {

    public static void main(String args[])
    {
        Animal tommy = new Animal("Tommy","Tortoise",2,0.2);
        Hare harry = new Hare("Harry",12,2,0,5,20);
        ArrayList<Animal> dash = new ArrayList<>();
        dash.add(tommy);
        dash.add(harry);

        Animal speedy = new Animal("Speedy","Tortoise",2,0.5);
        Hare thumper = new Hare("Thumper",10,1.5,0,60,80);
        Dog doug = new Dog("Doug",6.5,0.75,0,200);
        ArrayList<Animal> warmup = new ArrayList<>();
        warmup.add(speedy);
        warmup.add(thumper);
        warmup.add(doug);

        Animal creepy = new Animal("Creepy","Tortoise",2.1,1);
        Hare buggs = new Hare("Buggs",11,2.0,0,80,250);
        Dog pluto = new Dog("Pluto",9,0.5,0,600);
        Animal gary = new Animal("Gary","Snail",1,0.25);
        PhaseBeast leeroy = new PhaseBeast();
        ArrayList<Animal> main = new ArrayList<>();
        main.add(creepy);
        main.add(buggs);
        main.add(pluto);
        main.add(gary);
        main.add(leeroy);

        Race rDash = new Race("The 100-Foot Dash",100,dash);
        rDash.runRace();
        Race theWarmup = new Race("The Warmup",500,warmup);
        theWarmup.runRace();
        Race MainEvent = new Race("The Main Event",1000,main);
        MainEvent.runRace();

    }
}
