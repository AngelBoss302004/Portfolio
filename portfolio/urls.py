"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api.views import aboutview
from api.views import educationview
from api.views import projectview
from api.views import skillsview
from api.views import experianceview
from api.views import certificationview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',aboutview.as_view()),
    path('education/',educationview.as_view()),
    path('project/',projectview.as_view()),
    path('skills/',skillsview.as_view()),
    path('experiance/',experianceview.as_view()),
    path('certification/',certificationview.as_view())

]
