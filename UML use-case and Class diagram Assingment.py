'''PART 3'''
#first class function: passenger
class Passenger:
    def __init__(self, name, email, password, passport, id):
        self._name = name # name of passenger
        self._email = email #email of passenger
        self._password = password #password of the passenger for profile
        self._passport = passport #passport num of passenger
        self._id = id #ID of passenger wanting to travel

    # Getter methods for the attributes above
    def get_name(self):
        return self._name #name of passenger

    def get_email(self):
        return self._email #email of passenger

    def get_password(self):
        return self._password #passenger's passsword

    def get_passport(self):
        return self._passport #passenger's passport num

    def get_id(self):
        return self._id #passenger's ID

    # Setter method for passwords if passenger wants to modify
    def set_password(self, password):
        self._password = password

    # function to display staff profile/info, but passed
    def display_function(self):
        pass

#Second class function: airline staff
class AirlineStaff:
    def __init__(self, staff_id, name, role, date_hired, salary): #5 attributes for the airline staff
        self._staff_id = staff_id #ID of staff member
        self._name = name #name of the staff member
        self._role = role #their role in the plane (could be attendent, cleaner, co-pilot, or pilot)
        self._date_hired = date_hired #when the staff was hired
        self._salary = salary #the salary of the staff monlthy

    # Getter methods for staff attributes
    def get_staff_id(self):
        return self._staff_id

    def get_name(self):
        return self._name

    def get_role(self):
        return self._role

    def get_salary(self):
        return self._salary

    def get_date_hired(self):
        return self._date_hired

    # Setter methods for the airline staff attributes (things that could be modified)
    def set_staff_id(self, staff_id):
        self._staff_id = staff_id

#did not put name because no need

    def set_role(self, role):
        self._role = role

    def set_salary(self, salary):
        self._salary = salary

#did not put the date hired because no need (no modification would be required)

    # function to display staff profile and info but put it pass
    def display_function(self):
        pass

#Third class function: flight
class Flight:
    def __init__(self, flight_number, aircraft_type, from_airport, to_airport, departure_time, arrival_time):
        self._flight_number = flight_number #num of flight
        self._aircraft_type = aircraft_type #aircraft type
        self._from_airport = from_airport #from where the flight is
        self._to_airport = to_airport # where the flight will leaf; to which country
        self._departure_time = departure_time #when the plane willl depart
        self._arrival_time = arrival_time #when the flight will arrive at the destination

        #Getter methods for the ticket class that the passenger selects
    def get_flight_number(self):
        return self._flight_number

    def get_aircraft_type(self):
        return self._aircraft_type

    def get_from_airport(self):
        return self._from_airport

    def get_to_airport(self):
        return self._to_airport

    def get_departure_time(self):
        return self._departure_time

    def get_arrival_time(self):
        return self._arrival_time

    # Setter methods
    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def set_aircraft_type(self, aircraft_type):
        self._aircraft_type = aircraft_type

    def from_airport(self, from_airport):
        self._from_airport = from_airport

    def set_to_airport(self, to_airport):
        self._to_airport = to_airport

    def set_departure_time(self, departure_time):
        self._departure_time = departure_time

    def set_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time

    # function to display flight info, but passed
    def display_function(self):
        pass

#Fourth class function: ticket
class Ticket:
    #we have 7 attributes for the ticket as shown
    def __init__(self, ticket_id, passenger_name, seat_number, price, gate, class_of_travel, print_option):
        self._ticket_id = ticket_id #ID of ticket
        self._passenger_name = passenger_name #pasenger name on the ticket
        self._seat_number = seat_number #the seat num the passenger will sit on
        self._price = price #prcie of the ticket
        self._gate = gate #gate number that will lead to the plane
        self._class_of_travel = class_of_travel #type class o the plane (eco or business)
        self._print_option= print_option #option of getting the ticket, saving a copy online or pringting it on site

 #geetter methods for the ticket function
    def get_ticket_id(self):
        return self._ticket_id

    def get_passenger_name(self):
        return self._passenger_name

    def get_seat_number(self):
        return self._seat_number

    def get_price(self):
        return self._price

    def get_gate(self):
        return self._gate

    def get_class_of_travel(self):
        return self._class_of_travel

    def get_print_option(self):
        return self._print_option

    # setter methods for the ticket for calling/modifying
    def set_ticket_id(self, ticket_id):
        self._ticket_id = ticket_id

    def set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    def set_seat_number(self, seat_number):
        self._seat_number = seat_number

    def set_price(self, price):
        self._price = price

    def set_gate(self, gate):
        self._gate = gate

    def set_class_of_travel(self, class_of_travel):
        self._class_of_travel = class_of_travel

    def set_print_option(self, print_option):
        self._print_option = print_option

    # function to display ticket attributes, but passed
    def display_function(self):
        pass

'''PART 4'''
#diplaying actual test case of the figure given
class Boarding_Pass_ticket:
    def __init__(self, flight_number, passenger_name, seat_number, gate, from_here, to_here, fight_time, Boarding_till,
                 date):
        self._passenger_name = passenger_name  # passenger's name
        self._seat_number = seat_number  # their seatt number on the airplane
        self._gate = gate  # gate number to enter the aircraft
        self._flight_number = flight_number  # num of flight passenger choose
        self._from_here = from_here  # the innitial place where the pasenger is from
        self._to_here = to_here  # the destination the passenger wants to go to
        self._fight_time = fight_time  # the time of the flight
        self._Boarding_till = Boarding_till  # waiting time in the plane till boarding
        self._date = date  # the date of the flight

    # getter methods for the ticket function
    def flight_number(self):
        return self._flight_number

    def get_passenger_name(self):
        return self._passenger_name

    def get_seat_number(self):
        return self._seat_number

    def get_gate(self):
        return self._gate

    def get_from_here(self):
        return self._from_here

    def get_to_here(self):
        return self._to_here

    def get_fight_time(self):
        return self._fight_time

    def get_Boarding_till(self):
        return self._Boarding_till

    def get_date(self):
        return self._date

    # setter methods for the ticket for calling/modifying
    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    def set_seat_number(self, seat_number):
        self._seat_number = seat_number

    def set_gate(self, gate):
        self._gate = gate

    def set_from_here(self, from_here):
        self._from_here = from_here

    def set_tp_here(self, tp_here):
        self._to_here = to_here

    def set_fight_time(self, fight_time):
        self._fight_time = fight_time

    def set_Boarding_till(self, Boarding_till):
        self._Boarding_till = Boarding_till

    def set_date(self, date):
        self._date = date


# selecting the attributes from the figure given in the assingmnt with the information of nine attributes of the boarding ticket
ticket = Boarding_Pass_ticket("NA4321", "James SMITH", "09A", "03", "CHICAGO ORD", "NEW YORK JFK", "11:40", "11:20",
                              "06 DEC 20")
# output of everything we want to see
print("Boarding Pass ticket information in figure:-")
print("Passenger Name:", ticket.get_passenger_name())
print("From: ", ticket.get_from_here())
print("To: ", ticket.get_to_here())
print("Flight num:", ticket.flight_number())
print("Time of Flight:", ticket.get_fight_time())
print("Date of flight:")
print("Seat num:", ticket.get_seat_number())
print("Gate num:", ticket.get_gate())
print("Boarding till:", ticket.get_Boarding_till())