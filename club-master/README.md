# Сообщество JunovNet

## Инструменты
- Python 3.12
- Esmerald
- Edgy
- Postgres
- Alembic
- Docker


### Запустить сборку
```shell
docker compose -f api/docker-compose.dev.yml up --remove-orphans --build
```

```shell
docker exec club-api-1 python manage.py makemigrations
```

```shell
docker exec club-api-1 python manage.py createsuperuser
```

### Перейти по адресу
```
http:\\127.0.0.1:8000\
```
