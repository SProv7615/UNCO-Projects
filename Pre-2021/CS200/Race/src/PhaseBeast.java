public class PhaseBeast extends Animal
{
    private Boolean booTired, phased = false;
    private int howLongHasTheBeastBeenTired = 0;
    private double phaseDistance = 0;
    int warpDistance;
    public PhaseBeast(String strName_,double douRunningSpeed_,double douVariationofSpeed_,
                      double douCurrentPosition_, int warpDistance_, Boolean booTired_)
    {
        super(strName_,"Phase Beast", douRunningSpeed_,douVariationofSpeed_,douCurrentPosition_);
        this.warpDistance = warpDistance_;
        this.booTired = booTired_;
    }

    public PhaseBeast(String strName_,double douRunningSpeed_,double douVariationofSpeed_)
    {
        super(strName_,"Phase Beast", douRunningSpeed_,douVariationofSpeed_,0);
        this.warpDistance = 20;
        this.booTired = false;

    }

    public PhaseBeast()
    {
        super("Leeroy","Phase Beast", 8,2,0);
        this.warpDistance = 40;
        this.booTired = false;
    }

    private Boolean getTired()
    {
        return this.booTired;
    }

    private Boolean setTired(Boolean booSetTired)
    {
        booTired = booSetTired;
        return booTired;
    }

    private Double phaseWarp()
    {
        randomize(20);
        if(getRandom() == 0)
        {
            this.phaseDistance=randomize(this.warpDistance);
            douCurrentPosition+=phaseDistance;
            setTired(true);
            this.phased = true;
        }
        return douCurrentPosition;
    }

    private Boolean getPhased()
    {
        return phased;
    }

    private int tiredTimeUp()
    {
        howLongHasTheBeastBeenTired++;
        return howLongHasTheBeastBeenTired;
    }

    public double updatePosition()
    {
        this.phased = false;
        if(!booTired)
        {
            phaseWarp();
        }
        else
        {
            randomize(5);
            if(getRandom()==0)
            {
                setTired(false);
                howLongHasTheBeastBeenTired=0;
            }
            else
            {
                tiredTimeUp();
            }
        }

        int CoinToss = douRandomRun.nextInt(2);
        Double douRunVari = douRandomRun.nextDouble();
        if(booTired) {
            if (CoinToss == 0) {
                douCurrentVariation = .5*(douRunningSpeed - (douVariationofSpeed * douRunVari));
            } else {
                douCurrentVariation = .5*(douRunningSpeed + (douVariationofSpeed * douRunVari));
            }
        }
        else
        {
            if (CoinToss == 0) {
                douCurrentVariation = douRunningSpeed - (douVariationofSpeed * douRunVari);
            } else {
                douCurrentVariation = douRunningSpeed + (douVariationofSpeed * douRunVari);
            }
        }
        outputDisplay();
        updateTime();
        douCurrentPosition+=douCurrentVariation;
        return douCurrentPosition;
    }

    public void outputDisplay()
    {
        String strDisplay = "";
        if(phased)
        {
            strDisplay = String.format(" %8s  %5s  %6s%-2.0f  |",formatting(douCurrentPosition),formatting(douCurrentVariation),"Phase-",phaseDistance);
        }
        else if(booTired)
        {
            strDisplay = String.format(" %8s  %5s  %6s%-2d  |",formatting(douCurrentPosition),formatting(douCurrentVariation),"Tired-",howLongHasTheBeastBeenTired);
        }
        else
        {
            strDisplay = String.format(" %8s  %5s  %8s  |",formatting(douCurrentPosition),formatting(douCurrentVariation),""); //28
        }
        System.out.print(strDisplay);
    }

    public void aniIntro()
    {
        System.out.println("    Running Speed: " + this.getRunSpeed());
        System.out.println("    Variation of Speed: " + this.getRunSpeedVari());
        System.out.println("    Distance that can be warped: "+warpDistance);
        System.out.println();
    }
}
