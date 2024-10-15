from dataclasses import dataclass
from typing import List, Dict

from django.contrib.auth.models import User
from estate.models.city import City
from estate.models.district import District
from estate.models.street import Street
from estate.models.enums import TypeFlat

@dataclass
class FlatSearchDTO:
    author: User
    square: List[float]
    price: List[float]
    cities: List[City]
    districts: List[District]
    streets: List[Street]
    floor: List[int]
    number_of_storeys: List[int]
    type: List[TypeFlat]
    rooms:List[int]

@dataclass
class HouseSearchDTO:
    author: User
    square: List[float]
    price: List[float]
    cities: List[City]
    districts: List[District]
    streets: List[Street]
    area: List[float]
    type: List[TypeFlat]
    rooms:List[int]