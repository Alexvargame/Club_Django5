from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blog.models import Article, Category, Tag
from faker import Faker
import random
from django.utils.text import slugify


User = get_user_model()
class Command(BaseCommand):
    help = 'Generates 15 demo articles for user with ID 1'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Получаем пользователя с ID 1
        user = User.objects.get(id=1)

        # Создаем несколько категорий, если их нет
        categories = Category.objects.all()
        if not categories.exists():
            categories = [Category.objects.create(name=fake.word()) for _ in range(3)]

        # Создаем несколько тегов, если их нет
        tags = Tag.objects.all()
        if not tags.exists():
            tags = [Tag.objects.create(name=fake.word()) for _ in range(5)]

        # Генерируем 15 статей
        for i in range(15):
            title = fake.sentence(nb_words=6)
            content = fake.paragraph(nb_sentences=10)
            category = random.choice(categories)

            # Генерация уникального slug
            slug = slugify(title)
            while Article.objects.filter(slug=slug).exists():
                # Если slug уже существует, добавляем случайное число
                slug = f"{slug}-{random.randint(1, 1000)}"

            article = Article.objects.create(
                title=title,
                content=content,
                author=user,
                category=category,
                slug=slug  # Указываем уникальный slug
            )

            # Добавляем случайные теги к статье
            article.tags.set(random.sample(list(tags), k=random.randint(1, 3)))

            self.stdout.write(self.style.SUCCESS(f'Created article: {title} with slug: {slug}'))

        self.stdout.write(self.style.SUCCESS('Successfully created 15 demo articles!'))