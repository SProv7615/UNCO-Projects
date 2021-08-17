using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Montel
{
    class Vampire : Monster, IPhotosensitivity
    {
        public Vampire(string name) : base(name, "Vampire")
        {
            this.Name = name;
            Species = "Vampire";
        }

        public override void Ability()
        {
            Console.WriteLine("You better hope that the windows are all properly covered if you don't want to imitate a bonfire.");
        }
    }
}
