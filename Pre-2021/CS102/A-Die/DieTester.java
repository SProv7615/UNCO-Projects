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
public class DieTester
{
  public static void main(String args[])
  {
    //Instantiating variables.
    int menuRun = 0, rollTest = 0, comboRoll = 0;
    Boolean run = true;
    String response, menu = "";
    char question;
    ArrayList<Integer> rollArray = new ArrayList<>();
    //Creating the menu.
    menu+="Games: \n";
    menu+="____________________________________ \n";
    menu+="1) Roll a standard 6-sided die. (D6) \n";
    menu+="2) Roll a percentile die. (D100) \n";
    menu+="3) Roll a random month. (D12) \n";
    menu+="4) Roll a Monopoly Turn (2D6 added together) \n";
    menu+="5) Yahtzee (5D6 rolled together) \n";
    menu+="6) Other tests) \n";
    while ( run == true )
    {
      //Introduction
      System.out.println("Good news, everyone. It's time to unveil my latest invention.");
      System.out.println("I call it... The dice roller.");
      System.out.println("Have you ever gotten tired from simply rolling dice, and maybe /n annoyed at having to chase one down after it falls to the floor?");
      System.out.println("Well worry no longer! This invention will roll the dice for it!");
      System.out.println("Now go on, give it a try.");
      Scanner numReader = new Scanner(System.in);
      System.out.println("Pick from this list of options to choose the die best suited for your game.");
      System.out.println();
      //Posting the menu.
      System.out.println(menu);
      response = numReader.nextLine();
      menuRun = Integer.parseInt(response);
      
      //Die D6
      if (menuRun == 1)
      {
        Die runDie1 = new Die();
        rollTest = runDie1.roll();
        rollArray.clear();
        for (int a = 0; a < 10; a++)
        {
          rollArray.add(runDie1.roll());
        }
        System.out.println("Test 1: Six-Sided Die (D6)");
        System.out.println("Range: 1 to 6");
        System.out.println("Single number test: "+rollTest);
        System.out.println("Multiple Number Test: ");
        for (Integer a : rollArray)
        {
          System.out.print(a + " ");
        }
        System.out.println("");
      }
      //Percentile Die
      if (menuRun == 2)
      {
        Die runDie2 = new Die(100);
        rollTest = runDie2.roll();
        rollArray.clear();
        for (int a = 0; a < 10; a++)
        {
          rollArray.add(runDie2.roll());
        }
        System.out.println("Test 2: Roll a Percentile Die (D100)");
        System.out.println("Range: 1 to 100");
        System.out.println("Single number test: "+rollTest);
        System.out.println("Multiple Number Test: ");
        for (Integer a : rollArray)
        {
          System.out.print(a + " ");
        }
        System.out.println("");
      }
      //Month Die
      if (menuRun == 3)
      {
        Die runDie3 = new Die(12);
        rollTest = runDie3.roll();
        rollArray.clear();
        for (int a = 0; a < 10; a++)
        {
          rollArray.add(runDie3.roll());
        }
        System.out.println("Test 3: Roll a Random Month (D12)");
        System.out.println("Range: 1 to 12");
        System.out.println("Single number test: "+rollTest);
        System.out.println("Multiple Number Test: ");
        for (Integer a : rollArray)
        {
          System.out.print(a + " ");
        }
        System.out.println("");
      }
      //Monopoly Dice
      if (menuRun == 4)
      {
        comboRoll = 0;
        Die runDie4 = new Die();
        for (int a = 0; a < 2; a++)
        {
          rollTest = runDie4.roll();
          comboRoll += rollTest;
        }
        rollArray.clear();
        for (int a = 0; a < 10; a++)
        {
          rollArray.add(runDie4.roll() + runDie4.roll());
        }
        System.out.println("Test 4: Monopoly Roll! (2D6)");
        System.out.println("Range: 2 to 12");
        System.out.println("Single number test: "+comboRoll);
        System.out.println("Multiple Number Test: ");
        for (Integer a : rollArray)
        {
          System.out.print(a + " ");
        }
        System.out.println("");
      }
      //YahtzeeDice
      if (menuRun == 5)
      {
        int yahtzeeDie = 0;
        comboRoll = 0;
        Die runDie5 = new Die();
        for (int a = 0; a < 5; a++)
        {
          rollTest = runDie5.roll();
          comboRoll += rollTest;
        }
        rollArray.clear();
        for (int a = 0; a < 10d; a++)
        {
          int yahtzeeRoll = 0;
          for (int b = 0; b < 5; b++)
          {
            yahtzeeDie = runDie5.roll();
            yahtzeeRoll += yahtzeeDie;
          }
          rollArray.add(yahtzeeRoll);
        }
        System.out.println("Test 4: Yahtzee! Roll (2D6)");
        System.out.println("Range: 5 to 30");
        System.out.println("Single number test: "+comboRoll);
        System.out.println("Multiple Number Test: ");
        for (Integer a : rollArray)
        {
          System.out.print(a + " ");
        }
        System.out.println("");
      }
      //"More"
      if (menuRun == 6)
      {
        int dungeonRoll1, dungeonRoll2, dungeonRoll3;
        String readyRoll = ("Press enter to roll to determine your fate!");
        System.out.println("Hah! You wanted MORE? So sorry, there's nothing here.");
        System.out.println("But... You know what, I feel bad. Okay. I'll come up with something for you.");
        System.out.println("Okay, okay. Here we go.");
        System.out.println("You stand in an open field. The sky is a bright, vibrant blue, the sun glowing brightly \n and seemingly, the entire world is ablaze in gold from the grain that ripples \n in the pleasant breeze.");
        System.out.println("Three options are open to you: to the left is a bustling town, white smoke curling slowly into the air.");
        System.out.println("Ahead of you, the golden fields taper off into a forest that, despite the cheerful weather,\n still manages to send a shiver up your spine.");
        System.out.println("And to your right - and, you honestly have no idea how you failed to see it before now - lies several sprawling, massive mountains.");
        System.out.println(readyRoll);
        numReader.nextLine();
        Die DungeonDie1 = new Die(3);
        dungeonRoll1 = DungeonDie1.roll();
        System.out.println("You rolled a "+dungeonRoll1);
        if (dungeonRoll1 == 1)
        {
          System.out.println("You decide that the cheerful sounds of village life cannot be ignored. The calls of merchants\n and the resolute banging of a blacksmith hard at work tickling the ear.");
          System.out.println("You glance only briefly at the other paths you're denying yourself the right to tread. Maybe \n in another life, you think with only a tinge of melancholy.");
          System.out.println("Alas, that glance to the side proved a bit more costly than you might have expected. A tree \n root that had outlasted the tree itself was in just the right position \n to hook your foot, tripping you up. You staggered...");
          System.out.println("And fell, and fell, and fell as your staggered foot caught nothing, plunging you into a hole!");
          System.out.println("With no real way to prepare as you plunged into darkness, you slammed into the ground with a \n sickening thud and passed out, never to awaken again!");
          System.out.println("Oh dear. That was a bad way to start - and end - your journey. Alas, I'm not being paid for this.");
          System.out.println("In fact, I'm *paying* for this! Maybe next time don't be so cheap. Slip your DM some cash under the table.");
          System.out.println("Or maybe you'll be lucky and choose a different path next time.");
        }
        else if (dungeonRoll1 == 2)
        {
          System.out.println("You sally forthwith... at the speed of a slow walk. You're not in the best of shape, it's true, but still - it's just a walk!");
          System.out.println("As you approach the forest which had seemed so close, you realize that it took much longer to reach the woods than expected.");
          System.out.println("The sun has already started to set, casting everything in reddish-gold and growing shadows. Owls had already begun to hoot.");
          System.out.println("The howl of a wolf made you flinch in surprise! And as you flinched, something burst forth from the forest.");
          System.out.println("Press Enter: Roll a d4");
          numReader.nextLine();
          Die DungeonDie2 = new Die(4);
          int DungeonRoll2 = DungeonDie2.roll();
          System.out.println("You rolled a "+DungeonRoll2);
          if(DungeonRoll2 == 1)
          {
            System.out.println("A sprinting figure slams into your body, sending the both of you to the ground in a tumble! You groan piteously while the figure \n scrambled off of you, screaming about monsters and witches and other unintelligible babblings before running off into the shadow-swallowed fields.");
            System.out.println("Chest bruising and sore, you decide 'Maybe this is a bad idea.' So thinking, you turned back and headed home - the lucky, lone survivor of these twisting passages of fate.");
          }
          else if (DungeonRoll2 == 2)
          {
            System.out.println("A wolf sprints from the shadows, teeth bared in a rictus of fury and bloodlust!");
            System.out.println("Press Enter: Roll a d2");
            numReader.nextLine();
            Die DungeonDieCombat = new Die(2);
            int dungeonDieCombatRoll = DungeonDieCombat.roll();
            System.out.println("You rolled a "+dungeonDieCombatRoll);
            if (dungeonDieCombatRoll == 1)
            {
              System.out.println("The wolf took you unawares, the snarling, slavering beast burying its teeth into your neck!");
              System.out.println("Thankfully, you lost consciousness almost immediately, rather than having to deal with the beast \n enjoying its feast.");
            }
            else if (dungeonDieCombatRoll == 2)
            {
              System.out.println("You duck to the side and the wolf, seemingly out of its mind, continued running past you.");
              System.out.println("Clearly, there was an entity that hated you in this world, and you just barely avoided its \n anger.");
              System.out.println("Best to head home and avoid testing your luck too long.");
            }
            else if (DungeonRoll2 == 3)
            {
              System.out.println("Your mouth goes dry as you realize that it wasn't the entirety of a beast. It was just the head.");
              System.out.println("A monstrous, reptilian visage glared out with feral yellow eyes, slitted like a cat's but with far more malice.");
              System.out.println("Glowing, reddish-yellow saliva dripped from a gaping, multi-fanged maw, the 'liquid' hissing and sizzling as it \n struck the ground, cooling and becoming dark like magma with its heat spent.");
              System.out.println("Perhaps the head of this gigantic dragon would ignore you if you just stand still.");
              System.out.println("Roll a di-");
              System.out.println("The dragon strikes before you could roll, its initiative too great! Teeth half the size of your body snapped into and around your body.");
              System.out.println("The heat of that molten maw incinerates you before your terrified mind could even comprehend the massive pain of being immolated.");
              System.out.println("Needless to say, you died.");
            }
            else if (DungeonRoll2 == 4)
            {
              System.out.println("The crashing and shaking of the woods heralded... nothing.");
              System.out.println("Or not nothing. Hues and shapes that were alien began to bubble forth from the dark woods.");
              System.out.println("Trees contorted and twisted, branches curling into various geometric shapes that hurt the mind to stare at.");
              System.out.println("Your mind broke - or perhaps it was already broken before you even arrived here?");
              System.out.println("You scramble away like a beast, gibbering madly, frothing at the mouth as the world continues \n to change around you, a frightening morass of colors and shapes brought forth from the depths of your terrified psyche.");
            }
          }
        }
          else if (dungeonRoll1 == 3)
          {
            System.out.println("A lightning bolt strikes you before you can head towards the mountains. Your charred body lies \n in the field, a solemn reminder of the fickleness of the gods.");
          }
      }
      //Mockery
      else if (menuRun > 6)
      {
        System.out.println("So sorry. That... whatever you put... seems to not be an acceptable value.");
      }
      //Giving the option for more tests.
      System.out.println("Would you like to play again? Y/N");
      question = numReader.next().toUpperCase().charAt(0);
      if (question == 'Y')
      {
        run = true;
      }
      else if (question == 'N')
      {
        System.out.println("Goodbye!");
        run = false;
      }
      else
      {
        System.out.println("Good job. I didn't understand that - so this is goodbye.");
        run = false;
      }
    }
  }
}
