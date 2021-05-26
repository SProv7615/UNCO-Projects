/*******************************************************************************
*                           Assignment 3                                       *
*                                                                              *
* PROGRAMMER:       Stephen Provost                                            *
* CLASS:            CS102                                                      *
* ASSIGNMENT:       Assignment assig-3                                         *
* INSTRUCTOR:       Dean Zeller                                                *
* SUBMISSION DATE:  2/15/2019                                                  *
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
 
    
  public Die(int numSides_)
  {
    this.numSides = numSides_;
  }

  public Die()
  {
    this(6);
  }
  
  public int getCurrentValue()
  {
    return dieValue;
  }
  
  public String toString()
  {
    dieValueS = dieValue+"";
    return dieValueS;
  }
  
  public int roll()
  {
    Random rollV = new Random();
    dieValue = rollV.nextInt(numSides)+1;
    return dieValue;
  }
  
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
  
  public void reallycheat(int reallyCheat_)
  {
    this.reallyCheat = reallyCheat_;
    this.dieValue = reallyCheat;
    System.out.println("Huh. You're really desperate, aren't you? Well, ok. Whatever you say. I won't judge... too hard.");
  }
}
