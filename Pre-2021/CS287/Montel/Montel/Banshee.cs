using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Montel
{
    class Banshee : Monster, ILoud
    {
        public Banshee(string name) : base(name, "Banshee")
        {
            this.Name = name;
            Species = "Banshee";
        }

        public override void Ability()
        {
            Console.WriteLine("Your song heralds your coming... and everyone elses' leaving. If they don't escape, they're probably dead..");
        }
    }
}
