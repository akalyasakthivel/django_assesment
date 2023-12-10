
from django.urls import path
from crud_app.views import CRUD

urlpatterns = [
    path('create_candidate/',CRUD.create_candidate, name='create_candidate'),
    path('get_candidate/<int:id>',CRUD.get_candidate,name='get_candidate'),
    path('update_candidate/<int:id>',CRUD.update_candidate, name='update_candidate'),
    path('delete_candidate/<int:id>',CRUD.delete_candidate, name='delete_candidate'),

]
