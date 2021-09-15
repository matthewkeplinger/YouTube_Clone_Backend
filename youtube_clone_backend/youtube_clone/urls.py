from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentList.as_view())
    # path('comments-id/<str:video_id>/', views.CommentDetail.as_view()),
    # path('comments-like/<int:id>/', views.CommentLike.as_view()),
    # path('comments-dislike/<int:id>/', views.CommentDislike.as_view())
]