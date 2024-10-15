
from django.shortcuts import render, redirect
from real_estate.real_estate_service import RealEstateService

from estate.models.city import City
from estate.models.district import District
from estate.models.street import Street
from estate.models.comments import Comment

from estate.repositories import CityRepository, DistrictRepository, StreetRepository

from datetime import datetime
class ObjectCreateMixin:
    form = None
    template = None
    redirect_success = None
    redirect_lose = None
    model_dto = None
    rep = None
    def get(self,request):
        form = self.form(initial={'floor':1 , 'number_of_storeys': 1, 'square': 1,
                                       'price': 1, 'number_address_building': 1, 'number_address_appart': 1,
                                       },
                         city=CityRepository().list_cities(),
                         district=DistrictRepository().list_districts(),
                         street=StreetRepository().list_streets(),
                         )
        return render(request, self.template, {'form':form})

    def post (self, request):
        form = self.form(request.POST,
                         city=CityRepository().list_cities(),
                         district=DistrictRepository().list_districts(),
                         street=StreetRepository().list_streets()
                         )
        # form.cleaned_data.pop('city') - Пример

        if form.is_valid():
            id_object  = self.form.__name__[:self.form.__name__.find('Create')].lower()+'_'+datetime.now().strftime('%Y%m%d%H%M%S')
            data = self.model_dto(
                **form.cleaned_data,
                id_object = id_object,
                author = request.user,
                site_link = 'www.site.'+id_object
            )
            RealEstateService(self.rep()).create_object(data)
            return redirect(self.redirect_success)
        return redirect(self.redirect_lose)


class ObjectDetailMixin:
    model = None
    template = None
    rep = None
    def get(self,request, pk):
        obj = self.model.objects.get(id=pk)
        dto = RealEstateService(self.rep()).detail_object(obj)
        context = {
            self.model.__name__.lower(): dto.__dict__
        }
        return render(request, self.template, context=context)

class ObjectAllDetailMixin:
    model = None
    model_comment = None
    template = None
    rep = None
    form_user = None
    form_guest = None
    model_dto = None
    rep_comment = None

    def get(self,request, pk):
        obj = self.model.objects.get(id=pk)
        dto = RealEstateService(self.rep()).detail_object(obj)
        initial = {'real_state': self.model_comment.objects.get(id=pk).pk}
        if request.user.is_authenticated:
            initial['author'] = request.user.username
            form = self.form_user(initial=initial)
        else:
            form = self.form_guest(initial=initial)
        context = {
            self.model.__name__.lower(): dto.__dict__,
            'comments': RealEstateService(self.rep_comment()).list_objects_filter(obj),
            'form': form,
        }
        return render(request, self.template, context=context)
    def post(self,request, pk):
        obj = self.model.objects.get(id=pk)
        dto = RealEstateService(self.rep()).detail_object(obj)
        initial = {'real_state': self.model_comment.objects.get(id=pk).pk}
        if request.user.is_authenticated:
            initial['author'] = request.user.username
            form = self.form_user(request.POST, initial=initial)
        else:
            form = self.form_guest(request.POST, initial=initial)
        if form.is_valid():
            data = self.model_comment_dto(
                **form.cleaned_data
            )
            RealEstateService(self.rep_comment()).create_object(data)
            #messages.add_message(request, messages.SUCCESS, '')
            return redirect(request.get_full_path_info())
        else:
            form = form
            #messages.add_message(request, messages.WARNING, '')

        context = {
            self.model.__name__.lower(): dto.__dict__,
            'comments': RealEstateService(self.rep_comment()).list_objects_filter(obj),
            'form': form,
        }
        return render(request, self.template, context=context)


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_success = None
    model_dto = None
    rep = None
    def get(self,request, pk):
        obj = self.model.objects.get(id=pk)
        context ={
            self.model.__name__.lower(): obj
        }
        return render(request, self.template, context=context)

    def post (self, request,pk):
        obj = self.model.objects.get(id=pk)
        obj.__dict__.pop('_state')
        author = obj.__dict__.pop('author_id')
        distrcit = obj.__dict__.pop('district_id')
        city = obj.__dict__.pop('city_id')
        street = obj.__dict__.pop('street_id')
        data = self.model_dto(
            **obj.__dict__,
            author=author,
            city=city,
            district=distrcit,
            street=street,
        )
        RealEstateService(self.rep()).delete_object(data)
        return redirect(self.redirect_success)

class ObjectUpdateMixin:
    form = None
    model = None
    template = None
    redirect_success = None
    redirect_lose = None
    model_dto = None
    rep = None

    def get(self,request, pk):
        obj = self.model.objects.get(id=pk)
        form = self.form(initial=RealEstateService(self.rep()).detail_object(obj).__dict__,
                         city=CityRepository().list_cities(),
                         district=DistrictRepository().list_districts(),
                         street=StreetRepository().list_streets(),
                         )
        return render(request, self.template, {'form':form, self.model.__name__.lower(): obj})

    def post (self, request,pk):
        obj = self.model.objects.get(id=pk)
        form = self.form(request.POST,  initial=RealEstateService(self.rep()).detail_object(obj).__dict__,
                         city=CityRepository().list_cities(),
                         district=DistrictRepository().list_districts(),
                         street=StreetRepository().list_streets(),
                         )
        # form.cleaned_data.pop('city') - Пример
        if form.is_valid():
            # city_id = int(form.cleaned_data.pop('city'))
            # disrtict_id = int(form.cleaned_data.pop('district'))
            # street_id = int(form.cleaned_data.pop('street'))
            data = self.model_dto(
                **form.cleaned_data,
                id=obj.id,
                id_object=obj.id_object,
                created_at=obj.created_at,
                author = request.user,
                realestate_ptr_id=obj.realestate_ptr_id,
                site_link = obj.site_link,
                # city=City.objects.get(id=city_id),
                # district=District.objects.get(id=disrtict_id),
                # street=Street.objects.get(id=street_id)
            )
            RealEstateService(self.rep()).update_object(data)
            return redirect(self.redirect_success)
        return redirect(self.redirect_lose)