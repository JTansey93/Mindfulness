from django.contrib import admin
from django.urls import path
from affirmations.views import UserAffirmationtListView, AffirmationCreateView

urlpatterns = [
    path('<str:username>/', UserAffirmationtListView.as_view(template_name='affirmations/list.html'), name='affirmation-list'),
    path('create/', AffirmationCreateView.as_view(template_name='affirmations/create.html'), name='affirmation-create'),
]