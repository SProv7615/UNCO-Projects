using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPE11
{
    class Person
    {
        public Person(int intID, string strFirstName, string strLastName)
        {
            this.IntID = intID;
            this.StrFirstName = strFirstName;
            this.StrLastName = strLastName;
        }

        //Private attributes so that they can only be adjusted through the proper methods.
        private int IntID { get; set; }
        private string StrFirstName { get; set; }
        private string StrLastName { get; set; }


        //Polymorphism - there is a 'default' student that happens, which allows for additional changes with little issue.
        public Person()
        {
            IntID = 100000;
            StrFirstName = "";
            StrLastName = "";
        }
        public int GetID()
        {
            return IntID;
        }

        public string GetFirstName()
        {

            return StrFirstName;
        }

        public string GetLastName()
        {
            return StrLastName;
        }

        public int SetID(int newID)
        {
            IntID = newID;
            return IntID;
        }

        public string SetFirstName(string newFirstName)
        {
            StrFirstName = newFirstName;
            return StrFirstName;
        }

        public string SetLastName(string newLastName)
        {
            StrLastName = newLastName;
            return newLastName;
        }
    }
}
