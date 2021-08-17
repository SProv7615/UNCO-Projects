using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPE11
{
    class Program
    {
        static void Main(string[] args)
        {

            CourseList University = new CourseList();
            {
                DisplayMenu();
            }



            void DisplayMenu()
            {
                Console.WriteLine("Course Manager");
                Console.WriteLine("____________________________");
                Console.WriteLine("1): Create Course");
                Console.WriteLine("2): Enter Students into Course");
                Console.WriteLine("3): Remove Students from Course");
                Console.WriteLine("4): Remove Course");
                Console.WriteLine("5): Enter Student Grades for Course");
                Console.WriteLine("6): Grade Analytics");
                Console.WriteLine("7): Exit");
                var choice = int.Parse(Console.ReadLine());
                switch (choice)
                {
                    case 1:
                        {
                            Console.Clear();
                            Console.WriteLine("Course Creation:");
                            Console.WriteLine("________________");
                            Course temp = new Course();
                            temp.CourseCreation();
                            University.AddCourse(temp);
                            Console.Clear();
                            DisplayMenu();
                            break;
                        }
                    case 2:
                        {
                            Console.Clear();
                            Console.WriteLine("Add Students:");
                            Console.WriteLine("_____________");
                            University.AddStudentstoCourse();
                            Console.Clear();
                            DisplayMenu();
                            break;
                        }
                    case 3:
                        {
                            Console.Clear();
                            Console.WriteLine("Remove Students:");
                            Console.WriteLine("________________");
                            University.RemoveStudentsfromCourse();
                            Console.Clear();
                            DisplayMenu();
                            break;
                        }
                    case 4:
                        {
                            Console.Clear();
                            University.RemoveCourse();
                            Console.Clear();
                            DisplayMenu();
                            break;
                        }
                    case 5:
                        {
                            Console.Clear();
                            University.ChangeStudentsGrades();
                            Console.Clear();
                            DisplayMenu();
                            break;
                        }
                    case 6:
                        {
                            Console.Clear();
                            Console.WriteLine("University Analytics:");
                            Console.WriteLine("_____________________");
                            University.GradeAnalytics();
                            Console.Clear();
                            DisplayMenu();
                            break;
                        }
                    case 7:
                        {
                            Environment.Exit(0);
                            break;
                        }
                    default:
                        {
                            Console.WriteLine("You have entered an unknown command.");
                            break;
                        }
                }

            }
        }
    }
}
