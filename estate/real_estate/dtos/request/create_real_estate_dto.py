from dataclasses import dataclass

@dataclass
class CreateFlatDTO:
    author: int
    id_object: str
    description: str
    site_link: str
    square: float
    price: float
    city: str
    district: int
    street: str
    number_address_building: str
    number_address_appart: str
    floor: int
    number_of_storeys: int
    type: str
    rooms: int
@dataclass
class CreateHouseDTO:
    author: int
    id_object: str
    description: str
    site_link: str
    square: float
    price: float
    city: str
    district: int
    street: str
    number_address_building: str
    number_address_appart: str
    area: float
    type: str
    rooms: int
