from .dtos.request.create_real_estate_dto import CreateFlatDTO, CreateHouseDTO


class RealEstateService:
    def __init__(self, repository):
        self.repository = repository#FlatRepository()
    def create_object(self, dto) -> None:
        self.repository.create_object(dto)

    def detail_object(self, obj):
        return self.repository.detail_object(obj)

    def delete_object(self, dto):
        self.repository.delete_object(dto)

    def update_object(self, dto):
        self.repository.update_object(dto)

    def list_objects(self):
        return self.repository.list_objects()

    def list_objects_filter(self, filter):
        return self.repository.list_objects(filter)

    def user_list_objects(self, user):
        return self.repository.list_user_objects(user)

    def search_objects(self, data):
        return self.repository.search_objects(data)

    def create_search_request(self, dto):
        self.repository.create_search_request(dto)

    def create_comment(self, dto):
        self.repository.create_object(dto)