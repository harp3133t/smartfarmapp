from django.urls import path
from .views import *

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', FarmListView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/growth/', GrowthView.as_view(), name='growth'),
    path('<int:pk>/manage/', ManageView.as_view(), name='manage'),
]
