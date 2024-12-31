import pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})
df_cards = pd.read_csv("cards.csv",dtype=str).to_dict(orient = "records")
df_cards_security=pd.read_csv("card_security.csv",dtype=str)



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

class CreditCard:
    def __init__(self,number):
        self.number=number

    def validate(self,expiration,holder,cvc):
        card_data={"number":self.number,"expiration":expiration,
                   "cvc":cvc,"holder":holder}
        if card_data  in df_cards:
            return True
        else:
            return False

"""SecureCreditCard being child class inherits CreditCard parent class"""
"""self.number is being inherited from parent class"""
class SecureCreditCard(CreditCard):
    def authenticate(self,given_password):
        password=df_cards_security.loc[df_cards_security["number"] == self.number,"password"].squeeze()
        if password == given_password:
            return True
        else:
            print("Wrong password")
            return False





print(df)
hotel_ID=input("Enter the hotel id as input: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    credit_card = SecureCreditCard(number="1234")
    if credit_card.validate(expiration="12/26",holder="SAURABH SHARMA",cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name=input("Enter customer's name: ")
            reservation_ticket=ReservationTicket(cust_name=name,hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Passwords of credit card are not matching")
    else:
        print("There is a problem with your payment")
else:
    print("Hotel is not available")








# if __name__ == "__main__":
