/*******************************************************************************
*                           Assignment 5                                       *
*                                                                              *
* PROGRAMMER:       Stephen Provost                                            *
* CLASS:            CS102                                                      *
* ASSIGNMENT:       Assignment assig-5                                         *
* INSTRUCTOR:       Dean Zeller                                                *
* SUBMISSION DATE:  3/08/2019                                                  *
*                                                                              *
* DESCRIPTION:                                                                 *
* Dice. So many die and dice. More than you can shake a cup with.              *
*                                                                              *
* COPYRIGHT:                                                                   *
* This program is (c) 2019 Stephen Provost and Dean Zeller. This is original   *
* work, without use of outside sources.                                        *
*******************************************************************************/

import java.util.*;

public class Die
{
  //Creating initial variables
  private int numSides, cheat, reallyCheat, dieValue;
  private String dieValueS;
    
  Random dieToss = new Random();
 
  //Creating die object and defining it by number of sides.
  public Die(int numSides_)
  {
    this.numSides = numSides_;
  }
  //Creating default die object.
  public Die()
  {
    this(6);
  }
  //Creating method of getting current value.
  public int getCurrentValue()
  {
    return dieValue;
  }
  //To-string method.
  public String toString()
  {
    dieValueS = dieValue+"";
    return dieValueS;
  }
  //Roll method.
  public int roll()
  {
    Random rollV = new Random();
    dieValue = rollV.nextInt(numSides)+1;
    return dieValue;
  }
  
  //Here's your chance to cheat, you cheating cheater.
  public void cheat(int cheat_)
  {
    this.cheat = cheat_;
    if (cheat > 0 && cheat <= numSides)
    {
      this.dieValue = cheat;
    }
    else
    {
      System.out.println("Wow. You're really bad at cheating. Try again - that's how bad I feel for you.");
    }
  }
  
  //Now you can REALLY cheat.
  public void reallycheat(int reallyCheat_)
  {
    this.reallyCheat = reallyCheat_;
    this.dieValue = reallyCheat;
    System.out.println("Huh. You're really desperate, aren't you? Well, ok. Whatever you say. I won't judge... too hard.");
  }
}
