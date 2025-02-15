import requests

from .telegram import TelegramService
from consultation.dao import ClientRequestDAO, ServiceDAO

class ClientRequestService:
    def __init__(self):
        self.telegram_service = TelegramService(bot_token="YOUR_BOT_TOKEN", chat_id="YOUR_CHAT_ID")

    def create_client_request(self, name, email, telegram, service_slug, message):
        client_request = ClientRequestDAO.create_client_request(name, email, telegram, service_slug, message)

        # Формируем сообщение для Telegram
        service = ServiceDAO.get_service_by_slug(service_slug)
        telegram_message = (
            f"Имя: {name}\n"
            f"Email: {email}\n"
            f"Услуга: {service.name}\n"
            f"Telegram: {telegram}\n"
            f"Сообщение: {message}"
        )

        # Отправляем сообщение в Telegram
        self.telegram_service.send_message(telegram_message)

        return client_request