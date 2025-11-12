from django.urls import path
from . import views

urlpatterns = [
    path('', views.StatusAlllistview.as_view()),
    # path('status/<int:id>', views.StatusAlllistview.as_view()),
    # Add your URL patterns here
]