#from django.conf.urls import url, include
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_main'

urlpatterns = [
    path(r'^$', views.Todo_main.as_view(), name='todo_main'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)