from enum import Enum, IntEnum


class ScoreEnum(IntEnum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class AmenitiesEnum(Enum):
    bath = 'Bath'
    microwave = 'Microwave'
    washing_machine = 'Washing machine'
    balcony = 'Balcony'
    janitor = 'Janitor'
    parking_space = 'Parking space'


class StatusEnum(Enum):
    freely = 'Freely'
    booked = 'Booked'
    rented = 'Rented'

