package TheLagMaker;

import java.util.concurrent.Semaphore;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * class Person extends the Thread class.
 */
public class Person extends Thread{
    int IGender, ITime, ITCounter, ID;
    boolean isFinished;
    AtomicInteger personalTime;
    Semaphore localSem;

    /**
     * constructor for a new Person
     * @param iD Unique id of each person
     * @param iGender integer representation of gender 0 = male, 1 = female
     * @param iTime randomly generated time in the restroom range 3 to 7 inclusive
     * @param clockTime global time unit that allows synchronization of Persons waiting
     * @param iSemaphore semaphore used to acquire permit to use the restroom
     */
    public Person(AtomicInteger iD, int iGender, int iTime, AtomicInteger clockTime, Semaphore iSemaphore)
    {
        this.ID = iD.intValue();
        this.IGender = iGender;
        this.ITime = iTime;
        this.personalTime = clockTime;
        this.localSem = iSemaphore;
        isFinished = false;
        ITCounter = 0;
    }

    @Override
    public void run(){
        this.arrive();
        this.useFacilities(this.getITime());
        this.depart();
    }

    /**
     * attempt to acquire an open permit for the thread
     */
    private void arrive() {
        try {
            this.localSem.acquire();
        } catch (InterruptedException exc) {
            exc.printStackTrace();
        }
    }

    /**
     * @param iTime pass in the current time
     */
    private void useFacilities(int iTime) {
        int timeWhenDone = iTime + this.personalTime.intValue(); // add current time to time need
        while(timeWhenDone > this.personalTime.intValue()){
            // Use the facilities delays for time x
        }
    }

    /**
     * release the permit to be used by the next person
     */
    private void depart() {
        this.localSem.release();
    }

    // unused methods available for later need
/*
    public void setID(AtomicInteger ID) {
        this.ID = ID.intValue();
    }

    public void setIGender(int iGender) {
        this.IGender = iGender;
    }

    public void setITime(int iTime) {
        this.ITime = iTime;
    }
*/

    public int getID() {
        return ID;
    }

    public int getIGender() {
        return IGender;
    }

    public int getITime() {
        return ITime;
    }

    public boolean checkIfDone(){
        this.ITCounter++; // increments time in the restroom
        return this.ITCounter >= this.ITime; // returns if the counter is greater than or equals to the time in restroom
    }

    public String toString() {
        return(this.getID() + ": is a " + this.getIGender() +
                ", who went to the bathroom for "+ this.getITime() + " minutes");
    }
}