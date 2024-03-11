from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowerListList.as_view()),
    path('followers/<int:pk>', views.FollowerDetailDetail.as_view()),
]