package TheLagMaker;

import java.util.ArrayList;
import java.util.concurrent.Semaphore;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * class Restroom manages the gender state and number of stalls
 */
public class Restroom {
    int numOfStalls; // total stalls in the restroom
    int genderState; // 2 represents vacant, 0 male, 1 female
    int localTime; // time given to restroom from the scheduler globalTime
    AtomicInteger localClock; // local instance of global clock
    ArrayList<Person> relievers; // list of people in the restroom
    ArrayList<Person> theRelieved; // list of people who have left the restroom
    Semaphore semaphore; // semaphore with stall number permits available

    /**
     * constructor Restroom builds a new instance
     * @param numOfStalls inputs a stall count
     * @param clockTime passes in the global time
     */
    public Restroom(int numOfStalls, AtomicInteger clockTime)
    {
        this.numOfStalls = numOfStalls;
        this.genderState = 2;
        this.relievers = new ArrayList<>();
        this.theRelieved = new ArrayList<>();
        this.localClock = clockTime;
        this.semaphore = new Semaphore(this.numOfStalls);
    }

    /**
     * @return current restroom state (who gets to use it)
     */
    public String getGenderState()
    {
        if(this.genderState == 0)
        {
            return "Male";
        }
        else if(this.genderState == 1)
        {
            return "Female";
        }
        else
        {
            return "Vacant";
        }
    }

    public void setTime(int timeIn){
        this.localTime = timeIn;
    }

    public int getTime(){ return this.localTime; }

    /**
     * @param genderVal updates the gender state to the value in
     */
    public void setGenderState(int genderVal)
    {
        this.genderState = genderVal;
    }
    public ArrayList<Person> getTheRelieved(){
        return this.theRelieved;
    }

    public Semaphore getSemaphore(){ return this.semaphore; }

    /**
     * @return the number of available stalls in the restroom
     */
    public int lineCheck()
    {
        int vacantSeats = this.numOfStalls - this.relievers.size();
        if(vacantSeats == this.numOfStalls)
            setGenderState(2);
        return vacantSeats;
    }

    /**
     * @param luckyKneeClencher is a Person being admitted to the Restroom
     */
    public void addPerson(Person luckyKneeClencher)
    {
        String gender;
        // assume the restroom is empty and modify current gender to match the person
        // the check is accomplished in the scheduler
        this.setGenderState(luckyKneeClencher.getIGender());
        relievers.add(luckyKneeClencher);
        // store the current gender for the print statement
        if(luckyKneeClencher.getIGender() == 0){ gender = "M";  }
        else { gender = "F"; }
        System.out.printf("Time = %2d; Person %2d (%s) enters the facilities for %d minutes\n",
                this.getTime(), luckyKneeClencher.getID(), gender, luckyKneeClencher.getITime());

        luckyKneeClencher.start(); // starts the thread by triggering the run method in Person
    }

    public ArrayList<Person> getRelievers()
    {
        // return the list of people in the restroom for iteration of time
        return relievers;
    }

    /**
     * update the clock each person holds similarly to how we use the atomic clock in Boulder irl.
     * if the person is finished they are removed to a relieved list
     */
    public void incrementTime(){
        String gender;
        ArrayList<Person> tempList = new ArrayList<>();
        for (Person person: this.getRelievers()){
            if (person.checkIfDone()){
                this.theRelieved.add(person);
                if(person.getIGender() == 0){ gender = "M";  }
                else { gender = "F"; }
                System.out.printf("Time = %2d; Person %2d (%s) exits\n", this.getTime(), person.getID(), gender);
                tempList.add(person);
            }
        }
        if (tempList.size() > 0){
            for (Person person : tempList){
                this.getRelievers().remove(person);
            }
        }
        if (this.getRelievers().size() == 0){ this.setGenderState(2); }
    }

    /**
     * clears all list in Restroom to clean up memory usage.
     */
    public void clearList() {
        this.getTheRelieved().clear();
        this.getRelievers().clear();
    }
}
