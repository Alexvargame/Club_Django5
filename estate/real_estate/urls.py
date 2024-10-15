from django.urls import path
from .controllers import real_estates, create_object, detail_object, delete_object, update_object
from real_estate.service.search_objects import search_objects, search_statistic


urlpatterns = [
    path('create/flat/', create_object.FlatCreateView.as_view(), name="create_flat"),
    path('create/house/', create_object.HouseCreateView.as_view(), name="create_house"),
    path('', real_estates.RealEstateListView.as_view(), name="list_real_estates"),
    path('user/', real_estates.UserRealEstateListView.as_view(), name="list_user_real_estates"),
    path('flat/all/<int:pk>/', detail_object.FlatAllDetailView.as_view(), name='detail_flat_for_all'),
    path('flat/<int:pk>/', detail_object.FlatDetailView.as_view(), name='detail_flat'),
    path('flat/<int:pk>/delete/', delete_object.FlatDeleteView.as_view(), name='delete_flat'),
    path('flat/<int:pk>/update/', update_object.FlatUpdateView.as_view(), name='update_flat'),
    path('house/<int:pk>/', detail_object.HouseDetailView.as_view(), name='detail_house'),
    path('house/all/<int:pk>/', detail_object.HouseAllDetailView.as_view(), name='detail_house_for_all'),
    path('house/<int:pk>/delete/', delete_object.HouseDeleteView.as_view(), name='delete_house'),
    path('house/<int:pk>/update/', update_object.HouseUpdateView.as_view(), name='update_house'),

    path('search/flats/', search_objects.FlatSearchView.as_view(), name='search_flat'),
    path('search/houses/', search_objects.HouseSearchView.as_view(), name='search_house'),
    path('search/statistic/', search_statistic.SearchStatictic.as_view(), name='search_statistic'),

]
