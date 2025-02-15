from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from blog.models import  Category


class CategoryArticlesView(View):
    def get(self, request, category_id):
        # Получаем категорию по ID или возвращаем 404, если категория не найдена
        category = get_object_or_404(Category, id=category_id)

        # Получаем все статьи, связанные с этой категорией
        articles = category.article_set.all()
        categories = Category.objects.all()
        # Пагинация: 5 статей на страницу
        paginator = Paginator(articles, 5)
        page_number = request.GET.get('page')  # Получаем номер страницы из запроса
        page_obj = paginator.get_page(page_number)  # Получаем объект страницы

        # Рендерим шаблон с контекстом
        return render(request, 'blog/category_articles.html', {
            'category': category,
            #'articles': articles,
            'page_obj': page_obj,
            'categories': categories,
        })