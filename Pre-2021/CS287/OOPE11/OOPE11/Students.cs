using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPE11
{
    class Students : Person
        //Inherited Person class
    {
        public Students(int intID, string strFirstName, string strLastName) : base()
        {
            this.IntID = intID;
            this.StrFirstName = strFirstName;
            this.StrLastName = strLastName;
            this.Grade = 0m;
        }

        //Private attributes so that they can only be adjusted through the proper methods.
        private int IntID { get; set; }
        private string StrFirstName { get; set; }
        private string StrLastName { get; set; }
        
        private decimal Grade { get; set; }


        //Polymorphism - there is a 'default' student that happens, which allows for additional changes with little issue.
        public Students()
        {
            IntID = 100000;
            StrFirstName = "";
            StrLastName = "";
        }

        public void StudentInfo()
        {
            int ID = GetID();
            string FN = GetFirstName();
            string LN = GetLastName();
            Console.WriteLine("Student ID: " + ID + ": Student Name: " + FN + " " + LN + " : Grade: " + Grade);
        }

        public void AddStudent()
        {
            Console.WriteLine("Please input Student's ID");
            int stuID = int.Parse(Console.ReadLine());
            Console.WriteLine("Please input Student's First Name");
            string stuFN = Console.ReadLine();
            Console.WriteLine("Please input Student's Last Name.");
            string stuLN = Console.ReadLine();
            Students AddedStudent = new Students(stuID, stuFN, stuLN);
        }

        public decimal SetGrade()
        {
            Console.WriteLine("Please enter a grade for this student.");
            decimal newGrade = decimal.Parse(Console.ReadLine());
            if(newGrade >= 0 && newGrade <= 100)
            {
                Grade = newGrade;
            }
            else
            {
                Console.WriteLine("That grade is outside of the parameters. The grade must be between 0 to 100 - no A+'s.");
            }
            return Grade;
        }

        public decimal GetGrade()
        {
            return this.Grade;
        }
    }
}
