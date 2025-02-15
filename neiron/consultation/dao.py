from .models import ServiceModel, ClientRequest

class ServiceDAO:
    @staticmethod
    def get_all_services():
        return ServiceModel.objects.all()

    @staticmethod
    def get_service_by_slug(slug):
        return ServiceModel.objects.get(slug=slug.lower())

class ClientRequestDAO:
    @staticmethod
    def create_client_request(name, email, telegram, service_slug, message):
        service = ServiceDAO.get_service_by_slug(service_slug.lower())
        return ClientRequest.objects.create(
            name=name,
            email=email,
            telegram=telegram,
            service=service,
            message=message
        )