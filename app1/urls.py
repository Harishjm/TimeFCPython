"""Time_Analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path,include
from . import views
urlpatterns = [

    path('records1',views.records1,name="records1"),
    path('records2', views.records2, name="records2"),
    path('records3', views.records3, name="records3"),
    path('records4', views.records4, name="records4"),
    path('records5', views.records5, name="records5"),
    path('records6', views.records6, name="records6"),
    path('records7', views.records7, name="records7"),
    path('index',views.index,name="index"),
]
