from rest_framework import serializers

from estate.models.search_requests import SearchRequestFlat, SearchRequestHouse


class SearchRequestFlatSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchRequestFlat
        fields = (
            'author',
            'type',
            'cities',
            'districts',
            'streets',
            'floor',
            'number_of_storeys',
            'square',
            'price',
            'rooms',
            'created_at'
        )