"""todosubject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#from django.conf.urls import include, url
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_main.urls')),
    path('index/', include('todo_main.urls')),
    path('home/', include('todo_main.urls')),

    #board app
    path('board/', include('todo_board.urls')),
   # path('insert/', include('todo_board.urls')),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 'todo_main.urls'),
    path('index/', 'todo_main.urls'),
    path('home/', 'todo_main.urls'),

    #board app
    path('board/', 'todo_main.urls'),
]'''