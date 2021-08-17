package ThreadsWithoutLimits;

import java.io.PrintWriter;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.io.IOException;

public class Main {

    public static void main(String args[]) {
        ParentThread parentName;
        ArrayList<ParentThread> threadList = new ArrayList<>();
        long threadMakerStart = System.currentTimeMillis();
        for(int i = 0; i < 10; i++)
        {
            parentName = new ParentThread();
            parentName.setName("Parent-"+i);
            threadList.add(parentName);
        }
        Instant threadMakerEnd = Instant.now();
        Instant threadTesterStart = Instant.now();
        for(ParentThread theParents : threadList){
            theParents.start();
        }
        try {
            for(ParentThread theParents : threadList){
                theParents.join();
            }
        }
        catch(InterruptedException e)
        {
            System.out.println("Things have gone terribly wrong.");
        }
        Instant threadTesterEnd = Instant.now();
        double threadTestTime = Duration.between(threadTesterStart,threadTesterEnd).toMillis();
        try{
            PrintWriter writer = new PrintWriter("Final_Times.txt");
            writer.println("ThreadMaker Start Time: "+ threadMakerStart);
            writer.println("ThreadTester Time: "+ threadTestTime);
            writer.println(System.currentTimeMillis());
            writer.close();
        }
        catch(IOException e)
        {
            System.out.println("File dead.");
        }
        System.out.println(threadTestTime);

    }
}