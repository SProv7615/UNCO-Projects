using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Montel
{
    class Fishman : Monster, ISlimy
    {
        public Fishman(string name) : base(name, "Fishman")
        {
            this.Name = name;
            Species = "Fishman";
        }
        public override void Ability()
        {
            Console.WriteLine("You're easy to track down, considering the trail you leave everywhere you go, and sit.");
        }
    }
}
