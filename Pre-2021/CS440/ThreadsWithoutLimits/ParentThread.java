package ThreadsWithoutLimits;

import java.util.ArrayList;


class ParentThread extends Thread {
    private Thread t;
    private String named;
    private ArrayList<ChildThread> soManyBabehs;
    @Override
    public void run() {
        soManyBabehs = new ArrayList<>();
        System.out.println(System.currentTimeMillis() + ": " + "Making the child: " +  this.getName());
        try{
            for(int i = 0; i < 10; i++){
                System.out.println(System.currentTimeMillis() + ": " + this.getName() + " Creating child: " + i);
                soManyBabehs.add(new ChildThread("Child "+i+" of " + this.getName()));
            }
            Thread.sleep(100);
        } catch (InterruptedException e){
            System.out.println("Thread " + this.getName() + " interrupted.");
        }
        for(ChildThread baby:soManyBabehs)
        {
            baby.start();
        }
        try {
            for (ChildThread baby : soManyBabehs) {
                baby.join();
            }
        }
        catch(InterruptedException e){
                System.out.println("Your child could not be created.");
            }
        try{
            Thread.sleep(1);
        }
        catch(InterruptedException e)
        {
            System.out.println("The child has encountered an error.");
        }
        System.out.println(System.currentTimeMillis() + ": Thread " + this.getName() + " has completed.");
    }

    public void start() {
        System.out.println(System.currentTimeMillis() + ": " + "Starting up: "+this.getName());
        if (t == null) {
            t = new Thread (this, this.getName());
            t.start();
        }
    }

//    public String getName()
//    {
//        return named;
//    }
//
//    public void setName(String nameToBe)
//    {
//        this.named = nameToBe;
//    }
}
