from django.urls import path
from .views import TodosViewset

urlpatterns = [
    path('todos/', TodosViewset.as_view()),
    path('todos/<int:id>/', TodosViewset.as_view())
]