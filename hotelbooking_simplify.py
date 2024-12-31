import pandas
from abc import ABC,abstractmethod
#ABC is abstract base class

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "Barclays Company"
    """Above watermark is class variables"""
    """Instance Variables are hotel_id"""
    """Instance variables are coded inside the class and method"""
    """All below functions or methods used inside this class are instance methods"""

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls,data):
        return len(data)

class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass



class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        """Instance Variables are customer_name and hotel"""
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount*100


    #Magic methods overwriting
    def __eq__(self,other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


#Abstract class

class DigitalTicket(Ticket):
    def generate(self):
        return "Hello,this is ur digital tiket"




"""Value of class variables can be shared across multiple instances of the class whereas values of instance variables can vary depending on input of id"""
"""Properties is a method which behaves like variable"""
"""static method do not get self or cls arguments"""


"""Magic methods"""
# print("hello" == "Hi")
# print(("hello").__eq__("hi"))
# print(1+2)
# print((1).__add__(2))
# print(dir(str))



