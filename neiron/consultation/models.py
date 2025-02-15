from django.db import models



class ServiceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    slug = models.SlugField(unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name="Описание услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    for_customer = models.TextField(verbose_name='Для клиента', help_text='Каждый пункт с новой строки')
    benefit = models.TextField(verbose_name='Преимущества')
    features = models.TextField(verbose_name='Особенности', help_text='Каждый пункт с новой строки')
    duration = models.CharField(max_length=255, verbose_name='Длительность')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'services'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
class ClientRequest(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    telegram = models.CharField(max_length=255, verbose_name="Telegram")
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, verbose_name="Услуга")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Запрос от {self.name} ({self.email})"

    class Meta:
        db_table = 'client_requests'
        verbose_name = 'Запрос от клиента'
        verbose_name_plural = 'Запросы от клиента'
