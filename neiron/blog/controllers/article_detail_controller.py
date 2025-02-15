from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import render
from blog.models import Article, Category

class ArticleDetailView(View):
    template_name = 'blog/article_detail.html'

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        categories = Category.objects.all()
        comments = article.comments.filter(parent_comment=None)
        context = {
            'article': article,
            'categories': categories,
            'comments': comments,
        }
        return render(request, self.template_name, context)