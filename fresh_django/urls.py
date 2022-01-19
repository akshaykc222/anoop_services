"""fresh_django URL Configuration

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

from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from django.conf.urls import url
from api import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
admin.site.site_header  =  "Virtual Queue Admin Panel"  
admin.site.site_title  =  "Virtual Queue Admin Panel"
admin.site.index_title  =  "Virtual Queue Admin Panel"
router = routers.DefaultRouter()
# router.register(api)
schema_view = get_swagger_view(title="Swagger Docs")
urlpatterns = [
    # path('',schema_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    url('api/v1/rest-auth/', include('rest_auth.urls')),
    url('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    url('api/v1/account/', include('allauth.urls')),
    url('api/v1/accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
        name='account_confirm_email'),
]