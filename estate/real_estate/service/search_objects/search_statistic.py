from django.views import View
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from datetime import date
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from estate.models.search_requests import SearchRequestFlat, SearchRequestHouse
from real_estate.forms import ChoiceDateForm
from real_estate.dtos.response.search_real_estate_dto import FlatSearchDTO, HouseSearchDTO
from real_estate.repository import FlatRepository, HouseRepository, SearchFlatRepository, SearchHouseRepository

from real_estate.serializers import SearchRequestFlatSerializer

from .dictionaries import type_flat_dict, type_house_dict


class SearchStatictic(LoginRequiredMixin, View):
    # form = ChoiceDateForm
    # model = SearchRequestFlat
    # user = User
    # template = 'real_estate/search_statistic.html'
    # name_model = 'flats'
    # statistic_keys = ['type', 'cities', 'districts', 'streets', 'floor', 'number_of_storeys', 'price', 'rooms',
    #                   'square', 'area', 'author_id']


    def get(self, request):
        # filter_backends = [DjangoFilterBackend]
        # filterset_fields = []
        statistic_keys = ['type', 'cities', 'districts', 'streets', 'floor', 'number_of_storeys', 'price', 'rooms',
                                            'square', 'area', 'author_id']
        statistic_dict = dict.fromkeys(statistic_keys)
        if request.GET:
            form = ChoiceDateForm(request.GET, initial={'date_at': date(2024,1,1), 'date_to': date(2024,1,12)})
            if form.data.getlist('type_flat'):
                temp_dict = dict(type_flat_dict)


                for typ in form.data.getlist('type_flat'):
                    temp_dict[typ] = 1
                #     typstr = 'type_flat__'+typ+'__name'
                #     filterset_fields.append(typstr)
                # print(filterset_fields)
                #flats = SearchRequestFlat.objects.filter(*filterset_fields)
                flats = SearchRequestFlat.objects.filter(Q(type__FLAT=temp_dict['FLAT'])|Q(type__SMART_FLAT=temp_dict['SMART_FLAT']))
                print('ODJDJ', flats)
                temp_dict = dict(type_flat_dict)
                for flat in flats:
                    for key in flat.__dict__:
                        if key in statistic_dict.keys():
                            if not statistic_dict.get(key):
                                statistic_dict[key] = {}
                            if key == 'author_id':
                                value = User.objects.get(id=flat.__dict__[key])
                                if statistic_dict[key].get(value):
                                    statistic_dict[key][value] += 1
                                else:
                                    statistic_dict[key][value] = 1
                            else:
                                for value in flat.__dict__[key]:
                                    if statistic_dict[key].get(value):
                                        statistic_dict[key][value] += 1
                                    else:
                                        statistic_dict[key][value] = 1
            if form.data.getlist('type_house'):
                temp_dict = dict(type_house_dict)
                for typ in form.data.getlist('type_house'):
                   temp_dict[typ] = 1
                houses = SearchRequestHouse.objects.filter(Q(type__HOUSE=temp_dict['HOUSE'])|Q(type__HARF_HOUSE=temp_dict['HARF_HOUSE']))

                print('ODJDJ', houses)
                temp_dict = dict(type_house_dict)
                for house in houses:
                    for key in house.__dict__:
                        if key in statistic_dict.keys():
                            if not statistic_dict.get(key):
                                statistic_dict[key] = {}
                            if key == 'author_id':
                                value = User.objects.get(id=house.__dict__[key])
                                if statistic_dict[key].get(value):
                                    statistic_dict[key][value] += 1
                                else:
                                    statistic_dict[key][value] = 1
                            else:
                                for value in house.__dict__[key]:
                                    if statistic_dict[key].get(value):
                                        statistic_dict[key][value] += 1
                                    else:
                                        statistic_dict[key][value] = 1
            print(statistic_dict)
            return render (request, 'real_estate/search_statistic.html', {'form': form, 'stats': statistic_dict})
        else:
            form = ChoiceDateForm(initial={'date_at': date(2024, 1, 1), 'date_to': date(2024, 1, 12)})

            return render(request, 'real_estate/search_statistic.html', {'form': form})