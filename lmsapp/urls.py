from django.urls import path
from . import views

from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book', views.create_book, name='create_book'),
    path('view_books', views.view_books, name='view_books'),
    path('update_book/<id>', views.update_book, name ='update_book'),
    path('delete_book/<id>', views.delete_book, name = 'delete_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
