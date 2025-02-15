from django.core.paginator import Paginator

from django.views import View
from django.shortcuts import render

from blog.models import Article, Category

class ArticleListView(View):
    template_name = 'blog/article_list.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.select_related('author', 'category').prefetch_related('tags').all()
        categories = Category.objects.all()

        # Пагинация: 5 статей на страницу
        paginator = Paginator(articles, 5)
        page_number = request.GET.get('page')  # Получаем номер страницы из запроса
        page_obj = paginator.get_page(page_number)  # Получаем объект страницы

        context = {
            #'articles': articles,
            'page_obj': page_obj,
            'categories': categories,
        }

        return render(request, self.template_name, context)