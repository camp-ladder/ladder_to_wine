from django.urls import path
from . import views

app_name = 'wines'
urlpatterns = [
    path('<int:id>', views.wine_detail_view, name='wine_detail_view'),
    path('review/create/<int:id>', views.create_review, name='create_review'),
    path('review/edit/<int:id>', views.edit_review, name='edit_review'),
    path('review/delete/<int:id>', views.delete_review, name='edit_review'),
]


    