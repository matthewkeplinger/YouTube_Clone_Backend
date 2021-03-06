from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<str:video_id>/', views.CommentDetail.as_view()),
    path('comments/<int:pk>/delete/', views.CommentDetail.as_view()),
    path('comments/<int:pk>/likes/', views.CommentLike.as_view()),
    path('comments/<int:pk>/dislikes/', views.CommentDislike.as_view())
]