using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPE11
{
    class CourseList
    {

        CourseList(List<Course> liListOfCourses)
        {
            this.ListOfCourses = liListOfCourses;
        }

        public List<Course> ListOfCourses { get; set; }

        public CourseList()
        {
            ListOfCourses = new List<Course>();
        }

        public void AddCourse(Course whoo)
        {
            ListOfCourses.Add(whoo);
        }

        public void AddCourse()
        {
            Console.WriteLine("Please enter the course ID.");
            int cID = int.Parse(Console.ReadLine());
            Console.WriteLine("Please enter the course name.");
            string cName = Console.ReadLine();

            Course newCourse = new Course();
            newCourse.SetCourseID(cID);
            newCourse.SetCourseName(cName);

            ListOfCourses.Add(newCourse);
        }

        public void ShowCourses()
        {
            int i = 1;
            foreach (Course s in ListOfCourses)
            {
                Console.WriteLine(i + "): Course ID: " + s.GetCourseID() + " : Course Title: " + s.GetCourseName());
                i++;
            }
            Console.WriteLine();
        }
        public void RemoveCourse()
        {
            Console.WriteLine("Course Removal:");
            Console.WriteLine();
            ShowCourses();
            Console.WriteLine("Please enter the ID of the course you would like to remove.");
            int rCourseNum = int.Parse(Console.ReadLine());
            foreach (Course s in ListOfCourses)
            {
                if (s.GetCourseID() == rCourseNum)
                {
                    ListOfCourses.Remove(s);
                }
                else
                {

                }
            }
            Console.WriteLine("That particular course was not found.");
        }

        public void AddStudentstoCourse()
        {
            Console.WriteLine("Course Select:");
            Console.WriteLine();
            ShowCourses();
            Console.WriteLine("Please enter the ID of the course you would like to add a student to: ");
            int rCourseNum = int.Parse(Console.ReadLine());
            foreach (Course t in ListOfCourses)
            {
                if (t.GetCourseID() == rCourseNum)
                {
                    Console.WriteLine("Please enter the number of students you would like to add to " + t.GetCourseName());
                    int intNumTimes = int.Parse(Console.ReadLine());
                    for (int i = 0; i < intNumTimes; i++)
                    {
                        Console.Write(i + ": ");
                        t.AddStudent();
                    }
                    break;
                }
                else
                {

                }
                Console.WriteLine("That particular course was not found.");
            }
        }

        public void RemoveStudentsfromCourse()
        {
            Console.WriteLine("Course Select:");
            Console.WriteLine();
            ShowCourses();
            Console.WriteLine("Please enter the ID of the course you would like to remove a student from: ");
            int rCourseNum = int.Parse(Console.ReadLine());
            foreach (Course t in ListOfCourses)
            {
                if (t.GetCourseID() == rCourseNum)
                {
                    t.RemoveStudent();
                    break;
                }
                else
                {
                }
            }
            Console.WriteLine("That particular course was not found.");
        }

        public void ChangeStudentsGrades()
        {
            Console.WriteLine("Course Select:");
            Console.WriteLine();
            ShowCourses();
            Console.WriteLine("Please enter the ID of the course you would like to change a student's grade in: ");
            int rCourseNum = int.Parse(Console.ReadLine());
            foreach (Course t in ListOfCourses)
            {
                if (t.GetCourseID() == rCourseNum)
                {
                    t.StudentGrades();
                    break;
                }
                else
                {
                }
            }
            Console.WriteLine("That particular course was not found.");
        }

        public void GradeAnalytics()
        {
            Console.WriteLine("Course Select:");
            Console.WriteLine();
            ShowCourses();
            Console.WriteLine("Please enter the ID of the course you would like to get the analytics for: ");
            int rCourseNum = int.Parse(Console.ReadLine());
            foreach (Course t in ListOfCourses)
            {
                if (t.GetCourseID() == rCourseNum)
                {
                    t.GradeAverage();
                    t.GradeMax();
                    t.GradeMin();
                    t.GradeMedian();
                    t.GradePercents();
                    Console.WriteLine("Press enter to return back to the menu");
                    Console.ReadLine();
                    break;
                }
                else
                {
                }
            }
            Console.WriteLine("That particular course was not found.");

        }
    }
}
