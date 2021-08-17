using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPE11
{
    class Teacher : Person
        //Inherited all of the methods of Person - no new ones necessary for Teacher at this time.
    {
        public Teacher(int intID, string strFirstName, string strLastName) : base(intID,strFirstName,strLastName)
        {

        }



    }
}
