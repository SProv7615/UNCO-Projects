package TheLagMaker;

import TheLagMaker.input.UserNumberInput;
import TheLagMaker.input.UserStringInput;

import java.util.LinkedList;
import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;

/**
 *  Restroom Scheduler creates randomly gendered people
 *  at even intervals and sorts them into gendered queues
 *  to be allowed through a single gendered restroom in a
 *  presumably efficient manner.
 */
public class RestroomScheduler {

    // static attributes
    static Random randomSelector;
    static LinkedList<Person> maleQueue;
    static LinkedList<Person> femaleQueue;
    static final AtomicInteger orderId = new AtomicInteger();
    static int globalTime = 0;
    static final AtomicInteger clockTime = new AtomicInteger(0);
    static Restroom portapotty;

    /**
     * main method runs the scheduler program
     * @param args not used
     */
    public static void main(String[] args) {

        System.out.println("\nWelcome to Project 3 with Stephen Provost and Kevin Ritter");

        // main scope variables
        UserStringInput stringInput = new UserStringInput();
        UserNumberInput numberInput = new UserNumberInput();
        randomSelector = new Random(17); // <-- random seed input
        maleQueue = new LinkedList<>();
        femaleQueue = new LinkedList<>();
        orderId.set(0);
        int totalArrivals = 20;
        int delayTime = 10;
        int numStalls = 3;
        int arrivalSize = 5;

        /*
            Switch statement presents the main menu and then changes default
          */
        switch (stringInput.getStringInput(menuOptions())){
            case "A":
                // arrivalSize for this case is the default condition
                break;
            case "B":
                // arrivalSize for case B is the only parameter difference
                arrivalSize = 10;
                break;
            case "C":
                // arrivalSize for case C is the only parameter difference
                arrivalSize = 20;
                break;
            case "D":
                // case D allows for user inputs for all numbers
                System.out.println("Choose total arrivals between 1 and 5000.");
                totalArrivals = numberInput.getInputNum(1, 5000);
                System.out.println("Choose arrival size between 1 and 5000.");
                arrivalSize = numberInput.getInputNum(1, 5000);
                System.out.println("Choose a delay time between arrivals from 0 to 60 minutes.");
                delayTime = numberInput.getInputNum(0, 60);
                System.out.println("Choose number of total stalls from 2 to 6.");
                numStalls = numberInput.getInputNum(2, 6);
        }

        // create the restroom object of given size and with common clock
        portapotty = new Restroom(numStalls, clockTime);

        /*
            While loop adds new arrivals
         */
        while(portapotty.getTheRelieved().size() < totalArrivals) {
            if (globalTime % delayTime == 0 && orderId.intValue() < totalArrivals){
                newArrivals(arrivalSize);
            }
            if (portapotty.lineCheck() > 0) { // if a vacancy exists
                switch (portapotty.getGenderState()) { // check which gender has priority
                    case "Vacant":
                        // add Persons of the queue which contains the lowest priority number
                        if (maleQueue.size() == 0 && femaleQueue.size() > 0) {
                            addPatrons(femaleQueue);
                        } else if (maleQueue.size() > 0 && femaleQueue.size() == 0) {
                            addPatrons(maleQueue);
                        } else if (maleQueue.getFirst().getID() < femaleQueue.getFirst().getID()) {
                            addPatrons(maleQueue);
                        } else if (maleQueue.getFirst().getID() > femaleQueue.getFirst().getID()) {
                            addPatrons(femaleQueue);
                        } else {
                            System.out.println("Both queues empty.");
                        }
                        break;
                    case "Male":
                        // add new male Persons
                        if (maleQueue.size() > 0) {
                            addPatrons(maleQueue);
                        }
                        break;
                    case "Female":
                        // add new female Persons
                        if (femaleQueue.size() > 0) {
                            addPatrons(femaleQueue);
                        }
                        break;
                }
            }
            // increment global clock and update the restroom to reflect the new time
            globalTime++;
            portapotty.setTime(globalTime);
            portapotty.incrementTime();
        }

        // clean up and exit
        portapotty.clearList();
        System.exit(0);
    }

    /**
     * Static method new arrivals generates the new Persons and assigns random (by seed) genders
     * it is here that the queues are populated as well
     * @param arrivalCount passes in the total number of arrivals
     */
    public static void newArrivals(int arrivalCount){
        int time; // variable to hold a random restroom usage time
        for(int i = 0; i < arrivalCount; i++){
            time = randomSelector.nextInt(5) + 3; // bounded 3 - 7 inclusive
            if(randomSelector.nextInt(10) + 1 > 6){ // bounded 1 - 10 inclusive & > 6
                maleQueue.add(new Person(orderId, 0, time, clockTime, portapotty.getSemaphore()));
                // instantiate new male person and add to queue
                System.out.printf("Time = %2d; Person %2d (%s) arrives\n", globalTime, orderId.intValue(), "M");
            }
            else{
                femaleQueue.add(new Person(orderId, 1, time, clockTime, portapotty.getSemaphore()));
                // instantiate new female person and add to queue
                System.out.printf("Time = %2d; Person %2d (%s) arrives\n", globalTime, orderId.intValue(), "F");
            }
            orderId.getAndIncrement();
        }
    }

    /**
     * Static method add patrons moves person from queue to restroom
     * @param queueIn passes in either male or female queue to pull the next restroom user from
     */
    public static void addPatrons(LinkedList<Person> queueIn){
        while (queueIn.size() > 0 && portapotty.lineCheck() > 0){
            portapotty.addPerson(queueIn.removeFirst());
        }
    }

    /**
     * @return Main menu string
     */
    public static String menuOptions(){
        return "Please choose from the following options:\n" +
                "(a)    5 : DELAY(10) : 5 : DELAY(10) : 5 : DELAY(10) : 5\n" +
                "(b)   10 : DELAY(10) : 10\n" +
                "(c)   20\n" +
                "(d)   Choose your own numbers.\n";
    }
}

