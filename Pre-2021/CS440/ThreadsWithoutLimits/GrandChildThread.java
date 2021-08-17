package ThreadsWithoutLimits;

class GrandChildThread extends Thread {
    private Thread t;

    GrandChildThread(String name) {
        this.setName(name);
    }

    public void run() {
        System.out.println(System.currentTimeMillis() + ": " +"Thread " +  this.getName() + " has finished.");
    }

    public void start () {
        System.out.println(System.currentTimeMillis() + ": Creating Grandchild: " +  this.getName() );
        if (t == null) {
            t = new Thread (this, this.getName());
            t.start();
        }
    }
}
