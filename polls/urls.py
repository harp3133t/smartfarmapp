from django.urls import path
from .views import *

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', FarmListView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/growth/', GrowthView.as_view(), name='growth'),
    #path('growth/<int:pk>/add/', GrowthView, name='growthadd'),
    path('<int:pk>/manage', ManageView.as_view(), name='manage'),
    #path('<int:pk>/manage/add/', ManageView.as_view(), name='manageadd'),
    path('<int:pk>/env', EnvView.as_view(), name='env'),
    #path('<int:pk>/env/add/', EnvView.as_view(), name='envadd'),
    # ex: /polls/5/results/
##    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
##    path('<int:question_id>/survey/', views.survey, name='survey'),
]
