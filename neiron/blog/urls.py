from django.urls import path

from blog.controllers.article_list_controller import ArticleListView
from blog.controllers.article_filter_controller import CategoryArticlesView
from blog.controllers.article_detail_controller import ArticleDetailView
from blog.controllers.add_comment_controller import AddCommentView

urlpatterns = [
    path('category/<int:category_id>/', CategoryArticlesView.as_view(), name='category_articles'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<slug:slug>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('articles/<slug:slug>/comment/<int:parent_comment>.reply/', AddCommentView.as_view(), name='add_comment_reply'),

]
