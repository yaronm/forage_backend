from abc import ABC
from datetime import datetime

from battery.battery import Battery


class SpindlerBattery(Battery, ABC):
   def __init__(self, current_date:datetime, last_service_date:datetime):
      self.last_service_date = last_service_date
      self.current_date = current_date

   def needs_service(self) -> bool:
      service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
      return service_threshold_date < self.current_date
