from django.urls import path
from blogs import views

urlpatterns = [
    path(
        "",
        views.MainView.as_view(),
        name="mainview",
    ),
    path(
        "blogcreate/",
        views.BlogCreateView.as_view(),
        name="blogcreateview",
    ),
    path(
        "list/",
        views.BlogList.as_view(),
        name="bloglist",
    ),
    path(
        "<str:blog_name>/",
        views.BlogView.as_view(),
        name="blogview",
    ),
    path(
        "<str:blog_name>/category/",
        views.CategoryView.as_view(),
        name="categoryview",
    ),
    path(
        "<str:blog_name>/category/<int:category_id>/",
        views.CategoryView.as_view(),
        name="categoryview",
    ),
    path(
        "<str:blog_name>/write/",
        views.ArticleView.as_view(),
        name="articlecreateview",
    ),
    path(
        "<str:blog_name>/detail/",
        views.ArticleView.as_view(),
        name="articleview",
    ),
    path(
        "<str:blog_name>/detail/<int:article_id>/",
        views.ArticleDetailView.as_view(),
        name="articledetailview",
    ),
    path(
        "<int:article_id>/comments/",
        views.CommentView.as_view(),
        name="commentview",
    ),
    path(
        "comments/<int:comment_id>/",
        views.CommentView.as_view(),
        name="commentview",
    ),
    path(
        "<int:article_id>/comments/<int:comment_id>/",
        views.ReCommentView.as_view(),
        name="commentview",
    ),
    path(
        "subscribe/<str:blog_name>/",
        views.SubscribeView.as_view(),
        name="user_subscribe_view",
    ),
    path(
        "<int:user_id>/list/",
        views.BlogList.as_view(),
        name="bloglist",
    ),
]
