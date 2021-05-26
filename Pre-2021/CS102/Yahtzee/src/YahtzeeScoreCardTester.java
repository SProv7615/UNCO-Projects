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
* This program is (c) 2019 Stephen Provost and Kevin Ritter and Dean Zeller.   *
* This is original work, without use of outside sources.                       *
*******************************************************************************/
import java.util.*;
public class YahtzeeScoreCardTester
{
    public static void main(String args[])
    {
        Scanner endGameReader = new Scanner(System.in);
        Scanner theOneReader = new Scanner(System.in);
        boolean playGame = true;
        int intTurnCounter = 0;
        String strRowLister = "";

        while(playGame = true)
        {
            YahtzeeScoreCard singleGame = new YahtzeeScoreCard();
            for(intTurnCounter = 0; intTurnCounter < 13; intTurnCounter++)
            {
                singleGame.DisplayScoreSheet();
                String stringRowReader = "", strReRoll = "";
                System.out.println();
                System.out.println("Please enter any combination of 1, 2, 3, 4, and 5 if you want to reroll that particular dice. \n Otherwise, you can press enter " +
                        "to skip rolling any dice.");
                System.out.println();
                System.out.printf("Dice Roll #" + (1) + ": " + singleGame.getRoll() +"\n");
                for(int i = 0; i < 2; i++) {
                    strReRoll = theOneReader.nextLine();
                    System.out.println(strReRoll);
                    if (strReRoll.contains("1") || strReRoll.contains("2") || strReRoll.contains("3") || strReRoll.contains("4") || strReRoll.contains("5"))
                    {
                        System.out.println("Re-rolling: " + strReRoll);
                        if (strReRoll.contains("1")) {
                            singleGame.rollDice(true, false, false, false, false);
                        }
                        if (strReRoll.contains("2")) {
                            singleGame.rollDice(false, true, false, false, false);
                        }
                        if (strReRoll.contains("3")) {
                            singleGame.rollDice(false, false, true, false, false);
                        }
                        if (strReRoll.contains("4")) {
                            singleGame.rollDice(false, false, false, true, false);
                        }
                        if (strReRoll.contains("5")) {
                            singleGame.rollDice(false, false, false, false, true);
                        }
                        if (i <= 2)
                        {
                            System.out.printf("Dice Roll #" + (i + 2) + ": " + singleGame.getRoll());
                            System.out.println();
                        }
                    }
                    if (!strReRoll.contains("1") && !strReRoll.contains("2") && !strReRoll.contains("3") && !strReRoll.contains("4") && !strReRoll.contains("5") && strReRoll.contains("")) {
                        System.out.println("Rerolls Skipped.");
                        i = i+3;
                    }
                }
                System.out.printf("Final Roll: " + singleGame.getRoll());
                System.out.println();

                boolean boolRowChoice = true;
                while(boolRowChoice) {
                    System.out.println("Use in row: ");
                    stringRowReader = theOneReader.nextLine();
                    if (!stringRowReader.contains("1") && !stringRowReader.contains("2") && !stringRowReader.contains("3") && !stringRowReader.contains("4") && !stringRowReader.contains("5")
                            && !stringRowReader.contains("6") && !stringRowReader.contains("7") && !stringRowReader.contains("8") && !stringRowReader.contains("9") &&
                            !stringRowReader.contains("10") && !stringRowReader.contains("11") && !stringRowReader.contains("12") && !stringRowReader.contains("13"))
                    {
                        System.out.println("Terribly sorry, but you seem to have chosen a non-existent line. I shall be magnanimous enough to allow you a second chance.");
                    }
                    else if (stringRowReader.contains("13") && singleGame.intScoresArray.get(13) < 0)
                    {
                        singleGame.scoreChance();
                        System.out.println("Score of " + singleGame.intScoresArray.get(13) + " saved in row 13");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("12") && singleGame.intScoresArray.get(12) < 0)
                    {
                        singleGame.scoreYahtzee();
                        System.out.println("Score of " + singleGame.intScoresArray.get(12) + " saved in row 12");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("11") && singleGame.intScoresArray.get(11) < 0) {
                        singleGame.scoreLargeStraight();
                        System.out.println("Score of " + singleGame.intScoresArray.get(11) + " saved in row 11");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("10") && singleGame.intScoresArray.get(10) < 0) {
                        singleGame.scoreSmallStraight();
                        System.out.println("Score of " + singleGame.intScoresArray.get(10) + " saved in row 10");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("9") && singleGame.intScoresArray.get(9) < 0) {
                        singleGame.scoreFullHouse();
                        System.out.println("Score of " + singleGame.intScoresArray.get(9) + " saved in row 9");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("8") && singleGame.intScoresArray.get(8) < 0) {
                        singleGame.scoreFourKind();
                        System.out.println("Score of " + singleGame.intScoresArray.get(8) + " saved in row 8");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("7") && singleGame.intScoresArray.get(7) < 0) {
                        singleGame.scoreThreeKind();
                        System.out.println("Score of " + singleGame.intScoresArray.get(7) + " saved in row 7");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("6") && singleGame.intScoresArray.get(5) < 0)
                    {
                        singleGame.scoreSixes();
                        System.out.println("Score of " + singleGame.intScoresArray.get(5) + " saved in row 6");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("5") && singleGame.intScoresArray.get(4) < 0)
                    {
                        singleGame.scoreFives();
                        System.out.println("Score of " + singleGame.intScoresArray.get(4) + " saved in row 5");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("4") && singleGame.intScoresArray.get(3) < 0) {
                        singleGame.scoreFours();
                        System.out.println("Score of " + singleGame.intScoresArray.get(3) + " saved in row 4");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("3") && singleGame.intScoresArray.get(2) < 0)
                    {
                        singleGame.scoreThrees();
                        System.out.println("Score of " + singleGame.intScoresArray.get(2) + " saved in row 3");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("2") && singleGame.intScoresArray.get(1) < 0)
                    {
                        singleGame.scoreTwos();
                        System.out.println("Score of " + singleGame.intScoresArray.get(1) + " saved in row 2");
                        System.out.println();
                        break;
                    }
                    else if (stringRowReader.contains("1") && singleGame.intScoresArray.get(0) < 0) {
                        singleGame.scoreOnes();
                        System.out.println("Score of " + singleGame.intScoresArray.get(0) + " saved in row 1");
                        System.out.println();
                        break;
                    }
                }
                singleGame.bonusScore();
                singleGame.totalScore();

            }
            System.out.println("Game Over:");
            singleGame.DisplayScoreSheet();

            System.out.println();
            System.out.println("Press enter to play again.");
            System.out.println("");
            String repeat = endGameReader.nextLine();
            if (repeat == "")
            {
                playGame = true;
            }
            else
            {
                playGame = false;
            }

        }
    }
}
