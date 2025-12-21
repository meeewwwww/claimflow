from core.constants import DELAY_COMPENSATIONS
from core.models import Flight


class FlightHasNotArrivedYet(Exception):
    pass


class DelayCalculator:
    '''Calculates time and compensation for MSC (miss connection time). Only accepts Flight objects'''
    @classmethod
    def calculate_delay_time(cls, flight):
        if not isinstance(flight, Flight):
            raise TypeError(f"{cls.__name__} only accepts objects of type 'Flight'")
        if flight.departure_dt_fact and flight.arrival_dt_fact:
            if not flight.time_of_delay:
                td = flight.arrival_dt_fact - flight.arrival_dt_plan
                flight.time_of_delay = td
                flight.save()
            return flight.time_of_delay
        else:
            raise FlightHasNotArrivedYet

    @classmethod
    def calculate_delay_compensation(cls, flight):
        if not isinstance(flight, Flight):
            raise TypeError(f"{cls.__name__} only accepts objects of type 'Flight'")
        delay_hours = flight.time_of_delay.seconds / 3600
        if delay_hours >= 6:
            return DELAY_COMPENSATIONS['6_hours']
        if delay_hours >= 4:
            return DELAY_COMPENSATIONS['4_hours']
        if delay_hours >= 2:
            return DELAY_COMPENSATIONS['2_hours']
        if delay_hours >= 0:
            return DELAY_COMPENSATIONS['less_than_2_hours']
        return DELAY_COMPENSATIONS['no_delay']