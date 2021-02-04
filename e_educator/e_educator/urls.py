"""e_educator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from education import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('user/',views.loaduser),
    path('author/', views.loadauthor),
    path('admins/', views.loadadmin),
    path('e_educator/',views.load_e_educator),
    path('userregs/', views.loaduserregs),
    path('addadmin/',views.addadmin),
    path('adminlogin/',views.loadadminlogin),
    path('checkadminlogin/',views.checkadminlogin),
    path('forgotpassword/',views.loadforgotpassword),
    path('checkadminloginid/',views.checkadminloginid),
    path('checkrecoverpassword/', views.checkrecoverpassword),
    path('category/', views.loadcategory),
    path('addcategory/', views.addcategory),
    path('editcategory/', views.editcategory),
    path('updatecategory/', views.updatecategory),
    path('deletecategory/', views.deletecategory),
    path('subcategory/', views.loadsubcategory),
    path('addsubcategory/', views.addsubcategory),
    path('editsubcategory/', views.editsubcategory),
    path('updatesubcategory/', views.updatesubcategory),
    path('deletesubcategory/', views.deletesubcategory),
    path('city/', views.loadcity),
    path('addcity/', views.addcity),
    path('editcity/', views.editcity),
    path('updatecity/', views.updatecity),
    path('deletecity/', views.deletecity),
    path('state/', views.loadstate),
    path('addstate/', views.addstate),
    path('editstate/', views.editstate),
    path('updatestate/', views.updatestate),
    path('deletestate/', views.deletestate),
    path('country/', views.loadcountry),
    path('addcountry/', views.addcountry),
    path('editcountry/', views.editcountry),
    path('updatecountry/', views.updatecountry),
    path('deletecountry/', views.deletecountry),
    path('adminlogin/', views.loadadminlogin),
    path('adminregistration/', views.loadadminregistration),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

