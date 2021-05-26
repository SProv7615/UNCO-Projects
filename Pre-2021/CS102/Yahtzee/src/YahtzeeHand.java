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
* The Yahtzee Hand object, to keep track of all of those dicey hands.          *
*                                                                              *
* COPYRIGHT:                                                                   *
* This program is (c) 2019 Stephen Provost and Dean Zeller. This is original   *
* work, without use of outside sources.                                        *
*******************************************************************************/

import java.util.*;

public class YahtzeeHand
{
  ArrayList<Die> dice = new ArrayList<Die>();
  int numSides, numDice, cheatingDice;
  String diceVal;
  Die die;
  int dieValue;
  
/*******************************************************************************
* YahtzeeHand                                                                  *
*                                                                              *
* Purpose: Creating an array to create a number of dice!                       *
* Parameters:                                                                  *
*     numDice and numSides, to define a series of die.                         *
* Return Value:  describe-return-value                                         *
*******************************************************************************/
  
  public YahtzeeHand(int numDice_, int numSides_)
  {
    this.numSides = numSides_;
    this.numDice = numDice_;
    
    for (int b = 0; b < numDice; b++)
    {
       die = new Die();
       dice.add(die);
    }
  }
  
/*******************************************************************************
* YahtzeeHand                                                                  *
*                                                                              *
* Purpose: Ensuring that if no sides are chosen, 6 is preselected.             *
* Parameters:                                                                  *
*     numDice to define the amount of die in the array.                        *
* Return Value:  describe-return-value                                         *
*******************************************************************************/
  
  public YahtzeeHand(int numDice_)
  {
    this(numDice_,6);
  }

/*******************************************************************************
* YahtzeeHand                                                                  *
*                                                                              *
* Purpose: Ensuring that if no dice or sides are enumerated, 5 and 6 are       *
* preselected.                                                                 *
* Parameters:                                                                  *
*     None.                                                                    *
* Return Value:  describe-return-value                                         *
*******************************************************************************/  
  public YahtzeeHand()
  {
    this(5,6);
  }
  
/*******************************************************************************
* rollDice                                                                     *
*                                                                              *
* Purpose: To roll every dice in an array.                                     *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value:  describe-return-value                                         *
*******************************************************************************/
  public void rollDice()
  {
    for (Die r : dice)
    {
      r.roll();
    }
  }

/*******************************************************************************
* toString()                                                                   *
*                                                                              *
* Purpose: Enabling the values to be turned into a string.                     *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value:  describe-return-value                                         *
*******************************************************************************/
  public String toString()
  {
    diceVal = "";
    for (Die d : dice)
    {
      diceVal += d.getCurrentValue() + " ";
    }
    return diceVal;
  }
  
/*******************************************************************************
* countDice                                                                    *
*                                                                              *
* Purpose: How many of a particular number show up in a single roll.           *
* Parameters:                                                                  *
*     int cDice                                                                *
* Return Value:Returns a requested value, showing how many that value showed up*
*******************************************************************************/
  public int countDice(int cDice)
  {
    int count = 0;
    for (Die cd : dice)
    {
      if (cd.getCurrentValue() == cDice)
      count++;
    }
    return count;
  }

/*******************************************************************************
* setDice                                                                      *
*                                                                              *
* Purpose: Allows user/creator to set the values of each dice in an array.     *
* Parameters:                                                                  *
*     int first, second, third, fourth, fifth.                                 *
* Return Value:  describe-return-value                                         *
*******************************************************************************/
  public void setDice(int first,int second,int third,int fourth,int fifth)
  {
    this.dice.get(0).cheat(first);
    this.dice.get(1).cheat(second);
    this.dice.get(2).cheat(third);
    this.dice.get(3).cheat(fourth);
    this.dice.get(4).cheat(fifth);
  }
  
/*******************************************************************************
* faceValue                                                                    *
*                                                                              *
* Purpose: Enables the values of a number to be returned.                      *
* Parameters:                                                                  *
*     int n                                                                    *
* Return Value:  Returns the value a particular number times by that number    *
*******************************************************************************/
  public int faceValue(int n)
  {
    return n*countDice(n);
  }

/*******************************************************************************
* chanceValue                                                                  *
*                                                                              *
* Purpose: Getting the current value of the dice.                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value:  returns the number given by Chance                            *
*******************************************************************************/
  public int chanceValue()
  {
    int Chance = 0;
    for (Die d : dice)
    {
      Chance += d.getCurrentValue();
    }
    return Chance;
  }

/*******************************************************************************
* threeKindValue                                                               *
*                                                                              *
* Purpose: Ensuring that when there are three of a kind they're totalled up.   *
*                                                                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value:  returns either the chanceValue or 0.                          *
*******************************************************************************/
  public int threeKindValue()
  {
    for (int i = 0; i < numSides+1; i++)
    {
      if(countDice(i)==3)
      {
        return chanceValue();
      }
    }
    return 0;
  }

/*******************************************************************************
* fourKindValue                                                                *
*                                                                              *
* Purpose: Ensuring that when there are four  of a kind they're totalled up.   *
*                                                                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value: returns either the chanceValue or 0.                           *
*******************************************************************************/  
  public int fourKindValue()
  {
    for (int i = 0; i < numSides+1; i++)
    {
      if(countDice(i)==4)
      {
        return chanceValue();
      }
    }
    return 0;
  }

/*******************************************************************************
* fullHouse                                                                    *
*                                                                              *
* Purpose: Two bools meet in a bar and decide to hook up. The result is a full *
*house.                                                                        *
*                                                                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value: returns either 25 or 0.                                        *
*******************************************************************************/   
  public int fullHouse()
  {
    Boolean two = false;
    Boolean three = false;
    for (int i = 0; i < numSides+1; i++)
    {
      if(countDice(i)==2)
      {
      two = true;
      }
      if(countDice(i)==3)
      {
      three = true;
      }
    }
    if(two && three)
    {
      return 25;
    }
    else
    {
      return 0;
    }
  }
  
/*******************************************************************************
* smallStraightValue                                                           *
*                                                                              *
* Purpose: 3 if statements that, if there's a 1-4, 2-5, or 3-6 a value of 30 is*
* given. Else 0.                                                               *
*                                                                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value: returns either 30 or 0.                                        *
*******************************************************************************/
  public int smallStraightValue()
  {
    if(countDice(1)>=1 && countDice(2) >=1 && countDice(3)>=1 && countDice(4) >=1)
    {
      return 30;
    }
    else if(countDice(2)>=1 && countDice(3)>=1 && countDice(4)>=1 && countDice(5) >=1)
    {
      return 30;
    }
    else if (countDice(3)>=1 && countDice(4)>=1 && countDice(5)>=1 && countDice(6) >=1)
    {
      return 30;
    }
    else
    {
      return 0;
    }
  }
  
/*******************************************************************************
* largeStraightValue                                                           *
*                                                                              *
* Purpose: 2 if statements that, if there's a 1-5 or 2-6 a value of 40 is given*
*                                                                              *
*                                                                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value: returns either 40 or 0.                                        *
*******************************************************************************/
  public int largeStraightValue()
  {
    if(countDice(1)>=1 && countDice(2) >=1 && countDice(3)>=1 && countDice(4) >=1 && countDice(5) >=1)
    {
      return 40;
    }
    else if(countDice(2)>=1 && countDice(3)>=1 && countDice(4)>=1 && countDice(5) >=1 && countDice(6) >=1)
    {
      return 40;
    }
    else
    {
      return 0;
    }
  }

/*******************************************************************************
* yahtzeeValue                                                                 *
*                                                                              *
* Purpose: yahtzee what I am doing here? Gives a value of yahtzee. Congrats.   *
*                                                                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value: returns either 50 or 0.                                        *
*******************************************************************************/
  public int yahtzeeValue()
  {
    for (int i = 0; i < numSides+1; i++)
    {
      if(countDice(i)==5)
      {
        return 50;
      }
    }
    return 0;
  }
/*******************************************************************************
* reportLine                                                                   *
*                                                                              *
* Purpose: A long, ugly line that ensures that all of the values are commited  *
* to paper.                                                                    *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value: N/A                                                            *
*******************************************************************************/  
  public void reportLine(int lineNum)
  {
    System.out.printf("%2d.%13s%5d%5d%5d%5d%5d%5d%5d%5d%5d%5d%5d%5d%5d \n",lineNum,toString(),faceValue(1),faceValue(2),faceValue(3),faceValue(4),faceValue(5),faceValue(6),threeKindValue(),fourKindValue(),fullHouse(),smallStraightValue(),largeStraightValue(),yahtzeeValue(),chanceValue());
  }

/*******************************************************************************
* reportHeader                                                                 *
*                                                                              *
* Purpose: Gives a title, a description, and some attributes being tracked.    *
*                                                                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value: N/A                                                            *
*******************************************************************************/    
  public void reportHeader()
  {
    System.out.println("Yahtzee Hand Report");
    System.out.println("Creating 10 manual YahtzeeHand examples:");
    System.out.println("      Dice         1s   2s   3s   4s   5s   6s   3k   4k   FH   Sm   Lg   Yt   Ch ");
  }
  
/*******************************************************************************
* reportKilo                                                                   *
*                                                                              *
* Purpose: Gives a title, a description, and some attributes being tracked.    *
*                                                                              *
* Parameters:                                                                  *
*     N/A                                                                      *
* Return Value: N/A                                                            *
*******************************************************************************/ 
  public void reportKilo()
  {
    System.out.println("Running a Kilo of Yahtzee Hands");
    System.out.println("Output Omitted");
    System.out.println("                   1s   2s   3s   4s   5s   6s   3k   4k   FH   Sm   Lg   Yt   Ch ");
  }
}