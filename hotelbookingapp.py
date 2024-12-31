import pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})


class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id=hotel_id
        self.name=df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """Book a hotel by changing its availability to No"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv",index=False)


    def available(self):
        """checks if the hotel is available"""
        availablity = df.loc[df["id"] == self.hotel_id,"available"].squeeze()
        if availablity == "yes":
            return True
        else:
            return False






class ReservationTicket:
    def __init__(self,cust_name,hotel_object):
        self.cust_name=cust_name
        self.hotel=hotel_object
    def generate(self):
        content = f"""
       Thank you for your reservation.
       Here are your booking details,
       Name:{self.cust_name},
       Hotel_Name:{self.hotel.name}
       """
        return content


print(df)
hotel_ID=input("Enter the hotel id as input: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name=input("Enter customer's name: ")
    reservation_ticket=ReservationTicket(cust_name=name,hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available")








# if __name__ == "__main__":
