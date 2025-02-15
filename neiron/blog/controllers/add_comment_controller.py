from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Article, Comment
from blog.forms import AddCommentForm


class AddCommentView(LoginRequiredMixin, View):

    def post(self, request, slug, parent_comment=None):
        article = get_object_or_404(Article, slug=slug)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            if parent_comment:
                comment.parent_comment = Comment.objects.get(id=parent_comment)
            comment.save()
        return redirect('article_detail', slug=slug)
