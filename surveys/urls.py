from django.urls import path
from . import views
from . import models
app_name = 'surveys'
urlpatterns = [

    path('new/', views.CreateView.as_view(), name='create'),
    path('add/', views.add_survey, name='add'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='index'),
]
