
from django.shortcuts import render, redirect
from real_estate.real_estate_service import RealEstateService
from datetime import date

# from estate.models.city import City
# from estate.models.district import District
# from estate.models.street import Street

from estate.repositories import CityRepository, DistrictRepository, StreetRepository


from datetime import datetime
class ObjectSearchMixin:
    form = None
    template = None
    model_dto = None
    model_rep = None
    search_rep = None
    name_model = None
    initial = None



    def get(self, request):
        if request.GET:
            form = self.form(request.GET,
                cities=CityRepository().list_cities(),
                districts=DistrictRepository().list_districts(),
                streets=StreetRepository().list_streets()
            )
            data = form.data

            if self.model_dto.__name__ == 'FlatSearchDTO':
                dto = self.model_dto(
                    author=request.user,
                    square=[int(data['square_at']),int(data['square_to'])],
                    price=[int(data['price_at']),int(data['price_to'])],
                    cities=list(CityRepository().filter_cities(data.getlist('cities'))),
                    districts=list(DistrictRepository().filter_districts(data.getlist('districts'))),
                    streets=list(StreetRepository().filter_streets(data.getlist('streets'))),
                    floor=[int(data['floor_at']),int(data['floor_to'])],
                    number_of_storeys=[int(data['number_of_storeys_at']), int(data['number_of_storeys_to'])],
                    type=data.getlist('type'),
                    rooms=[int(data['rooms_at']),int(data['rooms_to'])]
                )
            elif self.model_dto.__name__ == 'HouseSearchDTO':
                dto = self.model_dto(
                    author=request.user,
                    square=[int(data['square_at']),int(data['square_to'])],
                    price=[int(data['price_at']),int(data['price_to'])],
                    cities=list(CityRepository().filter_cities(data.getlist('cities'))),
                    districts=list(DistrictRepository().filter_districts(data.getlist('districts'))),
                    streets=list(StreetRepository().filter_streets(data.getlist('streets'))),
                    area=[int(data['area_at']),int(data['area_to'])],
                    type=data.getlist('type'),
                    rooms=[int(data['rooms_at']),int(data['rooms_to'])]
                )
            print('DTO',dto)
            RealEstateService(self.search_rep()).create_search_request(dto)
            objs = RealEstateService(self.model_rep()).search_objects(dto)
            print('OBJS', objs)

            return render(request, self.template, {'form': form, self.name_model:objs})
        else:
            form = self.form(initial=self.initial,
                cities=CityRepository().list_cities(),
                districts=DistrictRepository().list_districts(),
                streets=StreetRepository().list_streets()
            )

            return render(request, self.template, {'form': form})

# class SearchStatisticMixin:
#     form = None
#     model = None
#     user = None
#     template = None
#     name_model = None
#     statistic_keys = None
#
#     def get(self, request):
#         # statistic_keys = ['type', 'cities', 'districts', 'streets', 'floor', 'number_of_storeys', 'price', 'rooms',
#         #                   'square', 'area', 'author_id']
#         statistic_dict = dict.fromkeys(self.statistic_keys)
#         if request.GET:
#             form = self.form(initial={'date_at': date(2024,1,1), 'date_to': date(2024,1,12)})
#
#             for obj in self.model.objects.all():
#
#                 for key in obj.__dict__:
#                     if key in statistic_dict.keys():
#                         if not statistic_dict.get(key):
#                             statistic_dict[key] = {}
#                         if key == 'author_id':
#                             value = self.user.objects.get(id=obj.__dict__[key])
#                             if statistic_dict[key].get(value):
#                                 statistic_dict[key][value] += 1
#                             else:
#                                 statistic_dict[key][value] = 1
#                         else:
#                             for value in obj.__dict__[key]:
#                                 if statistic_dict[key].get(value):
#                                     statistic_dict[key][value] += 1
#                                 else:
#                                     statistic_dict[key][value] = 1
#             print(statistic_dict)
#             return render (request, self.template, {'form': self.form, self.name_model: statistic_dict})
#         else:
#             form = self.form(initial={'date_at': date(2024, 1, 1), 'date_to': date(2024, 1, 12)})
#
#             return render(request, self.template, {'form': self.form})