from django.urls import path
from .views import CoutryCreateListView, RetriaveDeleteView

urlpatterns = [
    path('', CoutryCreateListView.as_view(), name='country_create_list'),
    path('<int:pk>/', RetriaveDeleteView.as_view(), name='country_retriave_delete')
]