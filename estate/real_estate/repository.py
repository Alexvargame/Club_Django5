
from estate.models.flat import Flat
from estate.models.house import House
from estate.models.city import City
from estate.models.district import District
from estate.models.street import Street
from estate.models.real_estate import RealEstate
from estate.models.enums import TypeFlat
from estate.models.comments import Comment

from estate.models.search_requests import SearchRequestFlat, SearchRequestHouse
from real_estate.dtos.response.detail_real_estate_dto import FlatDTO, HouseDTO
from real_estate.dtos.response.search_real_estate_dto import FlatSearchDTO, HouseSearchDTO

class FlatRepository:
    model = Flat

    def create_object(self, dto):
        flat = self.model.objects.create(
            type=dto.type,
            author=dto.author,
            id_object=dto.id_object,
            description=dto.description,
            site_link=dto.site_link,
            square=dto.square,
            rooms=dto.rooms,
            price=dto.price,
            number_address_building=dto.number_address_building,
            number_address_appart=dto.number_address_appart,
            floor=dto.floor,
            number_of_storeys=dto.number_of_storeys,
        )
        flat.city = dto.city#City.objects.get(id=int(dto.city))
        flat.district = dto.district#District.objects.get(id=int(dto.district))
        flat.street = dto.street#Street.objects.get(id=int(dto.street))
        flat.save()

    def update_object(self, dto):
        flat = self.model.objects.get(id=dto.id)
        for key, value in dto.__dict__.items():
            flat.__dict__[key]=value
        flat.save()
        # flat = self.model.objects.update(
        #     realestate_ptr_id=dto.realestate_ptr_id,
        #     created_at=dto.created_at,
        #     type=dto.type,
        #     author=dto.author,
        #     id_object=dto.id_object,
        #     description=dto.description,
        #     site_link=dto.site_link,
        #     square=dto.square,
        #     price=dto.price,
        #     number_address_building=dto.number_address_building,
        #     number_address_appart=dto.number_address_appart,
        #     floor=dto.floor,
        #     number_of_storeys=dto.number_of_storeys,
        #     city=dto.city,
        #     district=dto.district,
        #     street=dto.street,
        #     #realestate_ptr_id=dto.realestate_ptr_id,
        # )
        # flat.city = City.objects.get(id=int(dto.city))
        # flat.district = District.objects.get(id=int(dto.district))
        # flat.street = Street.objects.get(id=int(dto.street))
        #flat.save()

    def detail_object(self, obj):
        dto = FlatDTO(
            id=obj.id,
            type=obj.type,
            author=obj.author,
            id_object=obj.id_object,
            description=obj.description,
            site_link=obj.site_link,
            square=obj.square,
            rooms=obj.rooms,
            price=obj.price,
            number_address_building=obj.number_address_building,
            number_address_appart=obj.number_address_appart,
            floor=obj.floor,
            number_of_storeys=obj.number_of_storeys,
            city=obj.city,
            district=obj.district,
            street=obj.street,
            created_at=obj.created_at,
            realestate_ptr_id=obj.realestate_ptr_id
        )
        return dto

    def delete_object(self, dto):
        flat = self.model.objects.get(id=dto.id)
        flat.delete()

    def list_objects(self):
        return self.model.objects.all()

    def list_user_objects(self, user):
        return self.model.objects.filter(author=user)

    def search_objects(self, dto):

        get_objects=self.model.objects.filter(
            type__in=dto.type,
            author=dto.author,
            square__range=dto.square,
            rooms__range=dto.rooms,
            price__range=dto.price,
            floor__range=dto.floor,
            number_of_storeys__range=dto.number_of_storeys,
            city__in=[city.id for city in dto.cities],
            district__in=[dist.id for dist in dto.districts],
            street__in=[st.id for st in dto.streets]
        )
        return get_objects

class HouseRepository:
    model = House

    def create_object(self, dto):

        house = self.model.objects.create(
            type=dto.type,
            author=dto.author,
            id_object=dto.id_object,
            description=dto.description,
            site_link=dto.site_link,
            square=dto.square,
            rooms=dto.rooms,
            price=dto.price,
            number_address_building=dto.number_address_building,
            number_address_appart=dto.number_address_appart,
            area = dto.area
        )
        house.city = dto.city#City.objects.get(id=int(dto.city))
        house.district = dto.district#District.objects.get(id=int(dto.district))
        house.street = dto.street#Street.objects.get(id=int(dto.street))
        house.save()

    def detail_object(self, obj):
        dto = HouseDTO(
            id=obj.id,
            type=obj.type,
            author=obj.author,
            id_object=obj.id_object,
            description=obj.description,
            site_link=obj.site_link,
            square=obj.square,
            rooms=obj.rooms,
            price=obj.price,
            number_address_building=obj.number_address_building,
            number_address_appart=obj.number_address_appart,
            area=obj.area,
            city=obj.city,
            district=obj.district,
            street=obj.street,
            created_at=obj.created_at,
            realestate_ptr_id=obj.realestate_ptr_id
        )
        return dto

    def delete_object(self, dto):
        house = self.model.objects.get(id=dto.id)
        house.delete()

    def update_object(self, dto):
        house = self.model.objects.get(id=dto.id)
        for key, value in dto.__dict__.items():
            house.__dict__[key]=value
        house.save()

    def list_objects(self):
        return self.model.objects.all()

    def list_user_objects(self, user):
        return self.model.objects.filter(author=user)
    def search_objects(self, dto):
        get_objects=self.model.objects.filter(
            type__in=dto.type,
            author=dto.author,
            square__range=dto.square,
            rooms__range=dto.rooms,
            price__range=dto.price,
            area__range=dto.area,
            city__in=[city.id for city in dto.cities],
            district__in=[dist.id for dist in dto.districts],
            street__in=[st.id for st in dto.streets]
        )
        return get_objects
class SearchFlatRepository:
    model = SearchRequestFlat

    def create_search_request(self, dto):
        search_request = self.model.objects.create(
            author=dto.author,
            square=dto.square,
            price=dto.price,
            floor=dto.floor,
            number_of_storeys=dto.number_of_storeys,
            rooms=dto.rooms,
            cities = [c.name for c in dto.cities],
            districts = [d.name for d in dto.districts],
            streets = [s.name for s in dto.streets],
            type = dict.fromkeys([t for t in dto.type], 1)
        )


class SearchHouseRepository:
    model = SearchRequestHouse
    def create_search_request(self, dto):
        search_request = self.model.objects.create(
            author=dto.author,
            square=dto.square,
            price=dto.price,
            area=dto.area,
            rooms=dto.rooms,
            cities=[c.name for c in dto.cities],
            districts=[d.name for d in dto.districts],
            streets=[s.name for s in dto.streets],
            type= dict.fromkeys([t for t in dto.type], 1),
        )




