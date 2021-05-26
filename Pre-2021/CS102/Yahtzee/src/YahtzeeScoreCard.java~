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
public class YahtzeeScoreCard {

    //Variable creation.
    ArrayList<YahtzeeHand> intDiceRoll;

    int intOnesScore = -1, intTwosScore = -1, intThreesScore = -1, intFoursScore = -1, intFivesScore = -1, intSixesScore = -1,
            intBonusScore = -1, intThreeKindScore = -1, intFourKindScore = -1, intFullHouseScore = -1, intSmallStraightScore = -1,
            intLargeStraightScore = -1, intYahtzeeScore = -1, intChanceScore = -1, intTotalScore = 0;
    int turnCounter = 0, numCounter = 0;
    boolean BoolD1 = false, BoolD2 = false, BoolD3 = false, BoolD4 = false, BoolD5 = false;

    ArrayList<Integer> intScoresArray;

    //Behold the Scorecard!
    YahtzeeScoreCard() {
        YahtzeeHand yahDRoll;
        intScoresArray = new ArrayList<>();
        intScoresArray.add(intOnesScore);
        intScoresArray.add(intTwosScore);
        intScoresArray.add(intThreesScore);
        intScoresArray.add(intFoursScore);
        intScoresArray.add(intFivesScore);
        intScoresArray.add(intSixesScore);
        intScoresArray.add(intBonusScore);
        intScoresArray.add(intThreeKindScore);
        intScoresArray.add(intFourKindScore);
        intScoresArray.add(intFullHouseScore);
        intScoresArray.add(intSmallStraightScore);
        intScoresArray.add(intLargeStraightScore);
        intScoresArray.add(intYahtzeeScore);
        intScoresArray.add(intChanceScore);
        intScoresArray.add(intTotalScore);
        int turnCounter = 0;

        intDiceRoll = new ArrayList<>();
        for (int i = 0; i <= 12; i++) {
            yahDRoll = new YahtzeeHand();
            yahDRoll.rollDice();
            intDiceRoll.add(yahDRoll);
        }

    }
    //The to-string method that allows the rolls to be easily seen.
    public String getRoll()
    {
        return intDiceRoll.get(turnCounter).toString();
    }

    //The roll-dice method that enables the dice to be told which ones need to be re-rolled.
    public void rollDice(boolean boolD1, boolean boolD2, boolean boolD3, boolean boolD4, boolean boolD5) {
        this.BoolD1 = boolD1;
        this.BoolD2 = boolD2;
        this.BoolD3 = boolD3;
        this.BoolD4 = boolD4;
        this.BoolD5 = boolD5;

        {
            if (BoolD1) {
                this.intDiceRoll.get(turnCounter).dice.get(0).roll();
            }
            if (BoolD2) {
                this.intDiceRoll.get(turnCounter).dice.get(1).roll();
            }
            if (BoolD3) {
                this.intDiceRoll.get(turnCounter).dice.get(2).roll();
            }
            if (BoolD4) {
                this.intDiceRoll.get(turnCounter).dice.get(3).roll();
            }
            if (BoolD5) {
                this.intDiceRoll.get(turnCounter).dice.get(4).roll();
            }

        }
    }

    //The various score methods for ones through sixes.
    public void scoreOnes() {
        intOnesScore = intDiceRoll.get(turnCounter).faceValue(1);
        intScoresArray.set(0, intOnesScore);
        turnCounter++;
    }

    public void scoreTwos() {
        intTwosScore = intDiceRoll.get(turnCounter).faceValue(2);
        intScoresArray.set(1, intTwosScore);
        turnCounter++;
    }

    public void scoreThrees() {
        intThreesScore = intDiceRoll.get(turnCounter).faceValue(3);
        intScoresArray.set(2, intThreesScore);
        turnCounter++;
    }

    public void scoreFours() {
        intFoursScore = intDiceRoll.get(turnCounter).faceValue(4);
        intScoresArray.set(3, intFoursScore);
        turnCounter++;
    }

    public void scoreFives() {
        intFivesScore = intDiceRoll.get(turnCounter).faceValue(5);
        intScoresArray.set(4, intFivesScore);
        turnCounter++;
    }

    public void scoreSixes() {
        intSixesScore = intDiceRoll.get(turnCounter).faceValue(6);
        intScoresArray.set(5, intSixesScore);
        turnCounter++;
    }

    //The method to determine the bonus score.
    public void bonusScore() {
        intBonusScore = 0;
        int intScoreTracker = 0;
        for (int i = 0; i < 6; i++)
        {
            if(intScoresArray.get(i) >= 0) {
                intScoreTracker += intScoresArray.get(i);
                if (intScoreTracker >= 63) {
                    intBonusScore = 35;
                } else {
                    intBonusScore = 0;
                }
                intScoresArray.set(6, intBonusScore);
            }
        }
    }

    //The method to determine three and four of a kind.
    public void scoreThreeKind() {
        intThreeKindScore = intDiceRoll.get(turnCounter).threeKindValue();
        intScoresArray.set(7, intThreeKindScore);
        turnCounter++;
    }

    public void scoreFourKind() {
        intFourKindScore = intDiceRoll.get(turnCounter).fourKindValue();
        intScoresArray.set(8, intFourKindScore);
        turnCounter++;
    }

    //The FullHouse method.
    public void scoreFullHouse() {
        intFullHouseScore = intDiceRoll.get(turnCounter).fullHouse();
        intScoresArray.set(9, intFullHouseScore);
        turnCounter++;

    }

    //The small-straight.
    public void scoreSmallStraight() {
        intSmallStraightScore = intDiceRoll.get(turnCounter).smallStraightValue();
        intScoresArray.set(10, intSmallStraightScore);
        turnCounter++;
    }

    //the large-straight
    public void scoreLargeStraight() {
        intLargeStraightScore = intDiceRoll.get(turnCounter).largeStraightValue();
        intScoresArray.set(11, intLargeStraightScore);
        turnCounter++;
    }

    //Yahtzee for the lucky son-of-a-******* who get it.
    public void scoreYahtzee() {
        intYahtzeeScore = intDiceRoll.get(turnCounter).yahtzeeValue();
        intScoresArray.set(12, intYahtzeeScore);
        turnCounter++;
    }

    //Maybe you've got a chance.
    public void scoreChance() {
        intChanceScore = intDiceRoll.get(turnCounter).chanceValue();
        intScoresArray.set(13, intChanceScore);
        turnCounter++;
    }

    //Summing up the whooooooooooole score.
    public void totalScore() {
        intTotalScore = 0;
        for (int score = 0; score<14; score++ ) {
            if (intScoresArray.get(score) >= 0) {
                intTotalScore += intScoresArray.get(score);
            }
        }
        intScoresArray.set(14, intTotalScore);
    }

    //The sheet that displays the various scores saved in the array.
    void DisplayScoreSheet() {
        System.out.println("Turn: #" + (turnCounter+1) + " of 13");
        System.out.println();
        if (intScoresArray.get(0) >= 0)
            System.out.println("1. Ones: \t\t\t\t" + intScoresArray.get(0));
        else
            System.out.println("1. Ones: \t\t\t\t");
        if (intScoresArray.get(1) >= 0)
            System.out.println("2. Twos: \t\t\t\t" + intScoresArray.get(1));
        else
            System.out.println("2. Twos: \t\t\t\t");
        if (intScoresArray.get(2) >= 0)
            System.out.println("3. Threes: \t\t\t\t" + intScoresArray.get(2));
        else
            System.out.println("3. Threes: \t\t\t\t");
        if (intScoresArray.get(3) >= 0)
            System.out.println("4. Fours: \t\t\t\t" + intScoresArray.get(3));
        else
            System.out.println("4. Fours: \t\t\t\t");
        if (intScoresArray.get(4) >= 0)
            System.out.println("5. Fives: \t\t\t\t" + intScoresArray.get(4));
        else
            System.out.println("5. Fives: \t\t\t\t");
        if (intScoresArray.get(5) >= 0)
            System.out.println("6. Sixes: \t\t\t\t" + intScoresArray.get(5));
        else
            System.out.println("6. Sixes: \t\t\t\t");
        if (intScoresArray.get(6) >= 0)
            System.out.println("BONUS: \t\t\t\t\t" + intScoresArray.get(6));
        else
            System.out.println("BONUS: \t\t\t\t\t");
        if (intScoresArray.get(7) >= 0)
            System.out.println("7. 3-Kind: \t\t\t\t" + intScoresArray.get(7));
        else
            System.out.println("7. 3-Kind: \t\t\t\t");
        if (intScoresArray.get(8) >= 0)
            System.out.println("8. 4-Kind: \t\t\t\t" + intScoresArray.get(8));
        else
            System.out.println("8. 4-Kind: \t\t\t\t");
        if (intScoresArray.get(9) >= 0)
            System.out.println("9. Full House: \t\t\t" + intScoresArray.get(9));
        else
            System.out.println("9. Full House: \t\t\t");
        if (intScoresArray.get(10) >= 0)
            System.out.println("10. Small Straight: \t" + intScoresArray.get(10));
        else
            System.out.println("10. Small Straight: \t");
        if (intScoresArray.get(11) >= 0)
            System.out.println("11. Large Straight: \t" + intScoresArray.get(11));
        else
            System.out.println("11. Large Straight: \t");
        if (intScoresArray.get(12) >= 0)
            System.out.println("12. Yahtzee: \t\t\t" + intScoresArray.get(12));
        else
            System.out.println("12. Yahtzee: \t\t\t");
        if (intScoresArray.get(13) >= 0)
            System.out.println("13. Chance: \t\t\t" + intScoresArray.get(13));
        else
            System.out.println("13. Chance: \t\t\t");
        if (intScoresArray.get(14) >= 0)
            System.out.println("TOTAL: \t\t\t\t\t" + intScoresArray.get(14));
    }
}

