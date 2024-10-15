from dataclasses import dataclass

from django.contrib.auth.models import User
from estate.models.city import City
from estate.models.district import District
from estate.models.street import Street

@dataclass
class FlatDTO:
    id: int
    author: User
    id_object: str
    description: str
    site_link: str
    square: float
    created_at: str
    price: float
    city: City
    district: District
    street: Street
    number_address_building: str
    number_address_appart: str
    floor: int
    number_of_storeys: int
    type: str
    realestate_ptr_id: int
    rooms: int

@dataclass
class HouseDTO:
    id: int
    author: User
    id_object: str
    description: str
    site_link: str
    square: float
    price: float
    city: City
    district: District
    street: Street
    number_address_building: str
    number_address_appart: str
    area: float
    type: str
    created_at: str
    realestate_ptr_id: int
    rooms: int
