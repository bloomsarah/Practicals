from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi(Prius, 100), SilverServiceTaxi(Limo, 100, 2), SilverServiceTaxi(Hummer, 100, 4)]


    print(MENU)
    menu_choice = input(">>> ").lower()