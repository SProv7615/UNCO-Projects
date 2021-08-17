package ThreadsWithoutLimits;

import java.util.ArrayList;

class ChildThread extends Thread {
    private Thread t;
    private ArrayList<GrandChildThread> soManyGrandBabehs;

    ChildThread(String name) {
        this.setName(name);
    }

    public void run() {
//        soManyGrandBabehs = new ArrayList<>();
//        System.out.println(System.currentTimeMillis() + ": " +"Making the grandbabies: " +  this.getName());
//        try{
//            for(int i = 0; i < 1000; i++){
//                System.out.println(System.currentTimeMillis() + ": " +this.getName() + " Creating grandchild: " + i);
//                soManyGrandBabehs.add(new GrandChildThread("Child "+i+" of " + this.getName()));
//            }
//            Thread.sleep(50);
//        } catch (InterruptedException e){
//            System.out.println("Thread " + this.getName() + " interrupted.");
//        }
//        for(GrandChildThread grandbaby:soManyGrandBabehs)
//        {
//            grandbaby.start();
//        }
//        try {
//            for (GrandChildThread grandbaby : soManyGrandBabehs) {
//                grandbaby.join();
//            }
//        }
//        catch(InterruptedException e){
//            System.out.println("Your grandbabeh has finished their job.");
//        }
        try{
            Thread.sleep(1);
        }
        catch(InterruptedException e)
        {
            System.out.println("Something has gone wrong with the grandbabeh");
        }
        System.out.println(System.currentTimeMillis() + ": Thread " +  this.getName() + " just finished.");
    }

    public void start () {
        System.out.println(System.currentTimeMillis() + ": " +"Creating: " +  this.getName() );
        if (t == null) {
            t = new Thread (this, this.getName());
            t.start();
        }
    }
}
