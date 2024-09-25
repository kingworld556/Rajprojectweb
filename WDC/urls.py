from Raj.views import *
"""
URL configuration for WDC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path , include
from Raj.views import *
from RCU.views import *
from Food.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from indus.views import *
from emailbox.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("page/",page),
    path("contactus/",contact),
    path("aboutus/",about),
    path("get/",userget),
    path('post/',userpost),
    path("cal/",calculator),
    path("number_checker/",even_odd),
    path('result/',cal_marks),
    path('score/',mark),
    path("recipe/",recipe),
    path('delete_recipe/<id>/',delete_recipe),
    path('update_recipe/<id>/',update_recipe),
    path('login_page/',login_page),
    path('register/',register),
    path('logout/',logout_page),
    path('stud/',get_stud, name='stud'),
    path('students/<student_id>/marks/',see_marks, name='see_marks'),
    path('email/',include('emailbox.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()
