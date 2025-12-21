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
        default = [
            'В соответствии с ФАП-82 Вы имеете право на бесплатное:',
            'организацию хранения багажа;',
            'предоставление комнаты матери и ребенка пассажиру с ребенком в возрасте до 7 лет;'
        ]
        delay_hours = flight.time_of_delay.seconds / 3600
        if delay_hours >= 6:
            default += ['размещение в гостинице при ожидании отправления рейса более восьми часов - в дневное время и более шести часов - в ночное время, а также доставку пассажиров транспортом от аэропорта до гостиницы и обратно.']
            return default
        if delay_hours >= 4:
            default += ['обеспечение горячим питанием при ожидании отправления рейса более четырех часов. При дальнейшей задержке рейса питание предоставляется каждые 6 часов в дневное время и каждые 8 часов в ночное время.']
            return default
        if delay_hours >= 2:
            default += ['обеспечение прохладительными напитками, а также 2 телефонных звонка или 2 сообщения по электронной почте при ожидании отправления рейса более 2-х часов.']
            return default
        if delay_hours >= 0:
            default[-1] = '- предоставление комнаты матери и ребенка пассажиру с ребенком в возрасте до 7 лет.'
            return default
        else:
            default = []