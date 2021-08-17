using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPE11
{
    class Course
    {
        Course(int intID, string strTitle, List<Students> liRoster)
        {
            this.StrTitle = strTitle;
            this.IntID = intID;
            this.LiRoster = liRoster;
        }

        private int IntID { get; set; }
        private string StrTitle { get; set; }

        private List<Students> LiRoster { get; set; }

        //Polymorphism again, ensuring that a Course will still exist even if not all information is provided.
        public Course()
        {
            this.StrTitle = "Temporary";
            this.IntID = 111111;
            this.LiRoster = new List<Students>();
        }

        public string SetCourseName(string tempName)
        {
            this.StrTitle = tempName;
            return StrTitle;
        }

        public int SetCourseID(int tempID)
        {
            this.IntID = tempID;
            return IntID;
        }

        public int GetCourseID()
        {
            return IntID;
        }

        public string GetCourseName()
        {
            return StrTitle;
        }

        public void CourseCreation()
        {
            Console.WriteLine("Please enter a Course ID:");
            int cID = int.Parse(Console.ReadLine());
            Console.WriteLine("Please enter a Course Name");
            string cName = Console.ReadLine();

            SetCourseID(cID);
            SetCourseName(cName);
        }

        public void AddStudent()
        {
            Console.WriteLine();
            foreach (Students t in LiRoster)
            {
                t.StudentInfo();
            }
            Console.WriteLine();

            Students s = new Students();
            Console.WriteLine("Please enter a 6 digit integer for the student's ID.");
            int sInt = int.Parse(Console.ReadLine());
            Console.WriteLine();
            Console.WriteLine("Please enter the student's first name.");
            string sF = Console.ReadLine();
            Console.WriteLine();
            Console.WriteLine("Please enter the student's last name.");
            string sL = Console.ReadLine();
            Console.WriteLine();


            s.SetID(sInt);
            s.SetFirstName(sF);
            s.SetLastName(sL);
            LiRoster.Add(s);
            Console.Clear();
        }

        public void RemoveStudent()
        {
            Console.WriteLine();
            foreach (Students t in LiRoster)
            {
                t.StudentInfo();
            }
            Console.WriteLine();
            Console.WriteLine("Please enter the ID of the student you would like to remove.");
            int rStudentNum = int.Parse(Console.ReadLine());
            foreach (Students s in LiRoster)
            {
                if (s.GetID() == rStudentNum)
                {
                    LiRoster.Remove(s);
                    break;
                }
                else
                {
                    
                }
            }
            Console.WriteLine("That particular student was not found.");
        }

        public void StudentGrades()
        {
            Console.WriteLine();
            foreach (Students t in LiRoster)
            {
                t.StudentInfo();
            }
            Console.WriteLine();
            Console.WriteLine("Please enter the ID of the student you would like to change their grade.");
            int rStudentNum = int.Parse(Console.ReadLine());
            foreach (Students s in LiRoster)
            {
                if (s.GetID() == rStudentNum)
                {
                    s.SetGrade();
                    break;
                }
                else
                {

                }
            }
            Console.WriteLine("That particular student was not found.");
        }

        public void GradeAverage()
        {
            decimal totalSum = 0m;
            int count = 0;
            foreach (Students t in LiRoster)
            {
                totalSum = totalSum + t.GetGrade();
                count++;
            }
            decimal decAverage = totalSum / count;
            Console.WriteLine("The average of students' grades for this class is: " + decAverage);
            
        }

        public void GradeMin()
        {
            decimal lowestGrade = 200;
            foreach (Students s in LiRoster)
            {
                if (s.GetGrade() <= lowestGrade)
                {
                    lowestGrade = s.GetGrade();
                    Console.WriteLine("Student with the lowest Grade: ");
                    s.StudentInfo();
                }
            }
        }

        public void GradeMax()
        {
            decimal highestGrade = 0;
            foreach (Students s in LiRoster)
            {
                if (s.GetGrade() >= highestGrade)
                {
                    highestGrade = s.GetGrade();
                    Console.WriteLine("Student with the highest grade: ");
                    s.StudentInfo();
                }
            }
        }

        public void GradeMedian()
        {
            decimal medianGrade = 0;
            List<Students> sortedList = LiRoster;
            sortedList.Sort((x, y) => x.GetGrade().CompareTo(y.GetGrade()));
            int halfway = (sortedList.Count() / 2);
            int underhalfway = ((sortedList.Count() / 2) - 1);
            if ((sortedList.Count() % 2) == 0)
            {
                Console.WriteLine("Two students are tied with the median grades: ");
                sortedList[underhalfway].StudentInfo();
                sortedList[halfway].StudentInfo();
            }
            else
            {
                medianGrade = sortedList[halfway].GetGrade();
                Console.WriteLine("The median grade is: " + medianGrade + ". It belongs to: ");
                sortedList[halfway].StudentInfo();
            }          
        }

        public void GradePercents()
        {
            int As = 0, Bs = 0, Cs = 0, Ds = 0, Fs = 0;
            int total = LiRoster.Count();
            foreach(Students s in LiRoster)
            {
                if(s.GetGrade() >= 90)
                {
                    As = As + 1;
                    Console.WriteLine(As);
                }
                else if(s.GetGrade() >= 80)
                {
                    Bs = Bs + 1;
                }
                else if (s.GetGrade() >= 70)
                {
                    Cs = Cs + 1;
                }
                else if (s.GetGrade() >= 60)
                {
                    Ds = Ds + 1;
                }
                else
                {
                    Fs = Fs + 1;
                }
            }
            decimal perA = As/total * 100m;
            decimal perB = Bs/total * 100m;
            decimal perC = Cs/total * 100m;
            decimal perD = Ds/total * 100m;
            decimal perF = Fs/total * 100m;

            Console.WriteLine();
            Console.WriteLine("The percentage of students who have an A in your class is " + perA);
            Console.WriteLine();
            Console.WriteLine("The percentage of students who have a B in your class is " + perB);
            Console.WriteLine();
            Console.WriteLine("The percentage of students who have a C in your class is " + perC);
            Console.WriteLine();
            Console.WriteLine("The percentage of students who have a D in your class is " + perD);
            Console.WriteLine();
            Console.WriteLine("The percentage of students who have an F in your class is " + perF);
        }

    }
}
