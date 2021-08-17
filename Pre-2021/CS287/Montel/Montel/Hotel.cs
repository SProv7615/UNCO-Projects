using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Montel
{
    class Hotel
    {
        public Hotel(string strHotelName,List<Reservations> liListofReservations)
        {
            this.StrHotelName = strHotelName;
            this.LiListOfReservations = liListofReservations;
        }

        private string StrHotelName { get; set; }
        private List<Reservations> LiListOfReservations { get; set; }

        public void ListOfReservations()
        {
            foreach(Reservations monList in LiListOfReservations)
            {
                monList.DisplayReservation();
                
            }
        }
    }
}
