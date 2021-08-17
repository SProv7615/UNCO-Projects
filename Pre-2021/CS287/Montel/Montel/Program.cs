using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Montel
{
    class Program
    {
        static void Main(string[] args)
        {
            Vampire Vladimir = new Vampire("Vlad");
            Banshee Sylvanas = new Banshee("Sylvanas");
            Fishman Murgle = new Fishman("Murgle");
            Zombie Zed = new Zombie("Zed");

            Reservations VampRes = new Reservations(Vladimir, 01, "March 1st, 2019", "March 10th, 2019");
            VampRes.BookReservation();


            Reservations BansRes = new Reservations(Sylvanas, 02, "March 31st, 2019", "April 11th, 2019");
            BansRes.BookReservation();

            Reservations FishRes = new Reservations(Murgle, 03, "", "");
            FishRes.BookReservation();

            Reservations ZomRes = new Reservations(Zed, 04, "", "");
            ZomRes.BookReservation();

            List<Reservations> HotelReservations = new List<Reservations>();
            HotelReservations.Add(VampRes);
            HotelReservations.Add(BansRes);
            HotelReservations.Add(FishRes);
            HotelReservations.Add(ZomRes);


            Hotel Translyvania = new Hotel("Transylvania",HotelReservations);
            Translyvania.ListOfReservations();

            Console.ReadKey();

            
        }
    }
}
