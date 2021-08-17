using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Montel
{
    class Zombie : Monster, ILoud, IStinky
    {
        public Zombie(string name) : base(name, "Zombie")
        {
            this.Name = name;
            Species = "Zombie";
        }

        public override void Ability()
        {
            Console.WriteLine("Your putrid stench curdles the nosehairs of everyone you walk by.");
            Console.WriteLine("Your groans herald your coming... and your leaving. They pretty much just make sure everyone knows where you are.");
        }
    }
}
