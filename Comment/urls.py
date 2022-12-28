from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = {
    path('api/PostComment/', views.PostComment),
    path('api/UpdateComment/<int:CommentID>', views.UpdateComment),
    path('api/GetCommentByUser/<str:user_id>', views.GetCommentByUser),
    path('api/GetCommentByMediaId/<int:mid>', views.GetCommentByMediaId),
    path('api/GetNewComment/', views.GetNewComment),
}
