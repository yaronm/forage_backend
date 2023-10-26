from abc import ABC
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car

class CarFactory(ABC):
   def __init__():
      pass
   
   def create_calliope(current_date:datetime, last_service_date:datetime, current_mileage:int, last_service_mileage:int) -> Car:
      battery = SpindlerBattery(current_date, last_service_date)
      engine = CapuletEngine(current_mileage, last_service_mileage)
      return Car(engine, battery)
   def create_glissade(current_date:datetime, last_service_date:datetime, current_mileage:int, last_service_mileage:int) -> Car:
      battery = SpindlerBattery(current_date, last_service_date)
      engine = WilloughbyEngine(current_mileage, last_service_mileage)
      return Car(engine, battery)
   def create_palindrome(current_date:datetime, last_service_date:datetime, warning_light_on:bool):
      battery = SpindlerBattery(current_date, last_service_date)
      engine = SternmanEngine(warning_light_on)
      return Car(engine, battery)
   def create_rorschach(current_date:datetime, last_service_date:datetime, current_mileage:int, last_service_mileage:int) -> Car:
      battery = NubbinBattery(current_date, last_service_date)
      engine = WilloughbyEngine(current_mileage, last_service_mileage)
      return Car(engine, battery)
   def create_thovex(current_date:datetime, last_service_date:datetime, current_mileage:int, last_service_mileage:int) -> Car:
      battery = NubbinBattery(current_date, last_service_date)
      engine = CapuletEngine(current_mileage, last_service_mileage)
      return Car(engine, battery)