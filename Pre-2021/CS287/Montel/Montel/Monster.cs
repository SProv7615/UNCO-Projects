using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Montel
{
    class Monster
    {
        public Monster(string name, string species)
        {
            this.Name = name;
            this.Species = species;
        }
        public string Name { get; set; }
        public string Species { get; set; }

        public string GetName()
        {
            return Name;
        }

        public virtual void Ability()
        {
            
        }
    }
}
