using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Montel
{
    class Reservations
    {
        public Reservations (Monster generic, int intRoomNumber, string strStartDate, string strEndDate)
        {
            this.Generic = generic;
            this.IntRoomNumber = intRoomNumber;
            this.StrStartDate = strEndDate;
            this.StrEndDate = strEndDate;
        }

        private Monster Generic { get; set; }
        private int IntRoomNumber { get; set; }

        private string StrStartDate { get; set; }
        private string StrEndDate { get; set; }

        public void BookReservation()
        {
            BookStartDate();
            BookEndDate(); 
        }

        private string BookStartDate()
        {
            Console.WriteLine("Please enter the start date of " + Generic.Name + "'s vacation.");
            StrStartDate = Console.ReadLine();
            return StrStartDate;
        }

        private string BookEndDate()
        {
            Console.WriteLine("Please enter the end date of" + Generic.Name + "'s vacation.");
            StrEndDate = Console.ReadLine();
            return StrEndDate;
        }

        public void DisplayReservation()
        {
            Console.WriteLine(Generic.Name + " has a scheduled vacation in room " + IntRoomNumber + " starting on the " + StrStartDate + " and ending on the " + StrEndDate);
            Generic.Ability();
        }



    }
}
